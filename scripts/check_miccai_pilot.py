#!/usr/bin/env python3
"""Offline integrity check for the public MICCAI pilot metadata. No network, no downloads."""
from __future__ import annotations
import csv
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "corpora" / "miccai" / "pilot"
CATALOG = PILOT / "pilot_catalog.csv"
ALLOWED_STATUS = {
    "metadata_verified", "abstract_and_reviews_verified",
    "introduction_read", "fulltext_audited",
}
REQUIRED = {
    "source_id", "year", "title", "official_url", "official_pdf_url",
    "verification_status", "presentation_type",
}

def main() -> None:
    with CATALOG.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing column(s): {sorted(missing)}")
        records = list(reader)

    ids, urls = set(), set()
    for row in records:
        sid = row["source_id"].strip()
        if not sid.startswith("PAPER-"):
            raise ValueError(f"Bad source ID: {sid}")
        if sid in ids:
            raise ValueError(f"Duplicate ID: {sid}")
        ids.add(sid)
        year = row["year"].strip()
        if year not in {"2025", "2026"}:
            raise ValueError(f"Unexpected year: {year}")
        if not row["title"].strip():
            raise ValueError(f"Missing title for {sid}")
        if row["verification_status"] not in ALLOWED_STATUS:
            raise ValueError(f"Bad verification_status for {sid}")
        link = row["official_url"]
        pdf = row["official_pdf_url"]
        if urlparse(link).hostname != "papers.miccai.org":
            raise ValueError(f"Unofficial paper URL: {link}")
        if urlparse(pdf).hostname != "papers.miccai.org" or not pdf.endswith(".pdf"):
            raise ValueError(f"Unexpected PDF URL: {pdf}")
        if link in urls:
            raise ValueError(f"Duplicate official URL: {link}")
        urls.add(link)
        local_analysis = row.get("analysis_path", "").strip()
        if local_analysis and not (PILOT.parent / local_analysis).is_file():
            raise ValueError(f"Missing local analysis: {local_analysis}")
    print(f"OK: {len(records)} unique MICCAI pilot records; IDs/URLs/statuses checked.")
    print("NOTE: This does not validate scientific claims, source content or copyright.")

if __name__ == "__main__":
    main()
