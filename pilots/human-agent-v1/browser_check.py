"""Browser checks. Full mode fails on blocked navigation; render-only is explicit."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile
from playwright.sync_api import sync_playwright
import build

def check(out: Path, render_only: bool = False) -> dict:
    build.build(out)
    human = out / 'human'
    results = []
    with sync_playwright() as w:
        executable = os.environ.get('CHROMIUM_PATH') or shutil.which('chromium')
        options = {'headless': True}
        if executable:
            options['executable_path'] = executable
        browser = w.chromium.launch(**options)
        try:
            for name, width, height in [('desktop', 1365, 900), ('mobile', 390, 844)]:
                context = browser.new_context(viewport={'width': width, 'height': height}, accept_downloads=True)
                page = context.new_page()
                errors = []
                page.on('pageerror', lambda error: errors.append(str(error)))
                if render_only:
                    page.set_content((human/'lesson.html').read_text(), wait_until='load')
                else:
                    page.goto((human/'lesson.html').resolve().as_uri(), wait_until='load')
                assert page.locator('article.exercise').count() == 4
                assert page.locator('td[data-value-path]').count() == 9
                assert page.locator('details.answer[open]').count() == 0
                page.locator('details.answer summary').first.click()
                assert page.locator('details.answer[open]').count() == 1
                page.locator('#x1').fill('SYNTHETIC_BROWSER_TEST_NOT_LEARNER_DATA')
                checks = ['four exercises', 'nine metrics', 'answer toggle', 'input']
                if not render_only:
                    page.reload(wait_until='load')
                    assert page.locator('#x1').input_value() == 'SYNTHETIC_BROWSER_TEST_NOT_LEARNER_DATA'
                    with page.expect_download() as download:
                        page.locator('#export').click()
                    saved = Path(download.value.path()).read_text(encoding='utf-8')
                    assert 'SYNTHETIC_BROWSER_TEST_NOT_LEARNER_DATA' in saved
                    page.evaluate('localStorage.clear()')
                    checks += ['reload persistence in same browser context', 'actual download content']
                page.locator('#x1').fill('')
                page.evaluate("document.querySelectorAll('details').forEach(x=>x.open=false);document.documentElement.style.scrollBehavior='auto';window.scrollTo(0,0)")
                assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
                assert not errors, errors
                checks += ['no page-wide overflow', 'no JavaScript error']
                page.screenshot(path=str(out/'editorial'/f'lesson-{name}.png'))
                if render_only:
                    page.set_content((human/'report.html').read_text(), wait_until='load')
                else:
                    page.goto((human/'report.html').resolve().as_uri(), wait_until='load')
                assert page.locator('td[data-value-path]').count() == 9
                assert page.title() == '系统收益与机制解释，需要分开回答'
                assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
                assert not errors, errors
                checks += ['report metrics and title', 'report responsive layout']
                page.screenshot(path=str(out/'editorial'/f'report-{name}.png'))
                results.append({'viewport': name, 'checks': checks, 'result': 'pass'})
                context.close()
        finally:
            browser.close()
    report = {'mode': 'render_only' if render_only else 'file_navigation', 'results': results,
              'not_checked': ['cross-session persistence', 'hosted deployment', 'learning outcomes', 'independent scientific review'],
              'independent_agent_runs': 0}
    if render_only:
        report['not_checked'] += ['file navigation', 'reload persistence', 'actual download']
    build.write_json(out/'editorial/browser_validation.json', report)
    return report

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, default=Path(__file__).resolve().parent/'dist-browser')
    parser.add_argument('--render-only', action='store_true', help='Explicitly skip navigation, persistence and download; never a full-browser pass.')
    args = parser.parse_args()
    print(json.dumps(check(args.out.resolve(), args.render_only), ensure_ascii=False))
