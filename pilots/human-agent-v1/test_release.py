"""Integration regressions; no scientific or learner-effect claims."""
import importlib.util
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from types import SimpleNamespace

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('release_build', P / 'build.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.data = b.load(P / 'records.json')
        self.schema = b.load(b.SCHEMA)
        self.index = b.validate(self.data, self.schema)

    def test_required_format_support_available(self):
        self.assertTrue({'date-time', 'uri'}.issubset(b.FormatChecker().checkers))

    def test_missing_format_support_fails_closed(self):
        with patch.object(b, 'FormatChecker', return_value=SimpleNamespace(checkers={})):
            with self.assertRaisesRegex(ValueError, 'Missing JSON Schema format support'):
                b.validate(self.data, self.schema)

    def test_versioned_schema_path(self):
        self.assertEqual(b.SCHEMA.name, 'knowledge-record.v0.2.schema.json')

    def test_q_has_sources_only(self):
        pack = b.context('Q', self.index)
        self.assertEqual(len(pack['records']), 4)
        self.assertTrue(all(r['record_type'] == 'source' for r in pack['records']))
        self.assertEqual(pack['review_phase'], 'source_first')

    def test_q_has_no_answer_or_interpretation_payload(self):
        pack = b.context('Q', self.index)
        forbidden = {'interpretation', 'experiment', 'claim', 'language_move', 'teaching_item'}
        self.assertTrue(all(not forbidden.intersection(r) for r in pack['records']))

    def test_compare_requires_saved_fact_sheet(self):
        pack = b.context('Q_compare', self.index)
        self.assertEqual(len(pack['records']), 17)
        self.assertIn('separately saved Q fact sheet', pack['prerequisite'])
        self.assertIn('not a runtime access gate', pack['prerequisite'])

    def test_every_pack_explicitly_unlaunched(self):
        for role in [*b.TASKS, 'Q_compare']:
            self.assertEqual(b.context(role, self.index)['execution'],
                             {'state': 'not_launched', 'independent_agent_runs': 0})

    def test_nonfinite_metrics_rejected(self):
        for value in [math.nan, math.inf, -math.inf]:
            with self.subTest(value=value):
                data = b.load(P / 'records.json')
                r = next(r for r in data['records'] if r['record_type'] == 'experiment')
                r['experiment']['rows'][0]['metrics'][0]['value'] = value
                with self.assertRaises(ValueError):
                    b.validate(data, self.schema)

    def test_build_has_eight_packs_seven_roles(self):
        with tempfile.TemporaryDirectory() as d:
            m = b.build(Path(d))
            self.assertEqual(m['prepared_task_packs'], 8)
            self.assertEqual(m['workstream_roles'], 7)
            self.assertEqual(len(list((Path(d)/'agent').glob('*.json'))), 8)

    def test_different_human_titles(self):
        with tempfile.TemporaryDirectory() as d:
            b.build(Path(d))
            lesson = (Path(d)/'human/lesson.html').read_text()
            report = (Path(d)/'human/report.html').read_text()
            self.assertIn('<title>不再罗列模块，把研究关系写清楚</title>', lesson)
            self.assertIn('<title>系统收益与机制解释，需要分开回答</title>', report)

    def test_qmd_titles_match_products(self):
        with tempfile.TemporaryDirectory() as d:
            b.build(Path(d))
            text = (Path(d)/'human/report.qmd').read_text()
            self.assertIn('title: "系统收益与机制解释，需要分开回答"', text)

if __name__ == '__main__':
    unittest.main(verbosity=2)
