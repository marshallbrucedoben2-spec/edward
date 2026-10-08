#!/usr/bin/env python3
"""Check the CALL-FOR-HUNT ledger and print the deadline view.

Usage:
  python3 scripts/ledger.py check     # validate ledger/ledger.csv, exit 1 on errors
  python3 scripts/ledger.py upcoming  # listed calls, nearest hard deadline first
"""
import csv
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

LEDGER = Path(__file__).resolve().parent.parent / "ledger" / "ledger.csv"
WITA = timezone(timedelta(hours=8))
COLUMNS = ["id", "status", "for", "venue", "type", "hd_wita", "hd_note", "verified",
           "url", "read_on", "fee", "mode", "indexing", "great", "fit", "notes"]
STATUSES = {"listed", "handled", "dropped", "new"}
FOR = {"Edward", "John", "both"}
VERIFIED = {"VERIFIED", "LEAD", "carried"}


def parse_hd(value):
    """Return an aware datetime in WITA, or None for an empty (rolling) deadline."""
    if not value:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            hd = datetime.strptime(value, fmt)
        except ValueError:
            continue
        if fmt == "%Y-%m-%d":
            hd = hd.replace(hour=23, minute=59)
        return hd.replace(tzinfo=WITA)
    raise ValueError(f"bad hd_wita {value!r}")


def load():
    with LEDGER.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            raise SystemExit(f"header mismatch:\n  got  {reader.fieldnames}\n  want {COLUMNS}")
        return list(reader)


def check(rows):
    errors, seen = [], set()
    for n, r in enumerate(rows, start=2):
        where = f"line {n} ({r['id'] or '?'})"
        if not r["id"]:
            errors.append(f"{where}: empty id")
        elif r["id"] in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(r["id"])
        if r["status"] not in STATUSES:
            errors.append(f"{where}: status must be one of {sorted(STATUSES)}")
        if r["for"] not in FOR:
            errors.append(f"{where}: for must be one of {sorted(FOR)}")
        if r["verified"] not in VERIFIED:
            errors.append(f"{where}: verified must be one of {sorted(VERIFIED)}")
        if r["verified"] == "VERIFIED" and not r["url"]:
            errors.append(f"{where}: VERIFIED needs a url")
        try:
            parse_hd(r["hd_wita"])
        except ValueError as e:
            errors.append(f"{where}: {e}")
        if r["status"] == "dropped" and not r["notes"]:
            errors.append(f"{where}: a drop needs its reason in notes")
    return errors


def upcoming(rows):
    now = datetime.now(WITA)
    live = [r for r in rows if r["status"] in ("listed", "new")]
    dated = sorted((r for r in live if r["hd_wita"]), key=lambda r: parse_hd(r["hd_wita"]))
    for r in dated:
        hd = parse_hd(r["hd_wita"])
        days = (hd - now).total_seconds() / 86400
        flag = "PASSED" if days < 0 else f"{days:5.1f}d"
        note = f" [{r['hd_note']}]" if r["hd_note"] else ""
        print(f"{flag:>7}  {r['hd_wita']:<16}  {r['for']:<6}  {r['verified']:<8}  {r['venue']} — {r['type']}{note}")
    for r in live:
        if not r["hd_wita"]:
            print(f"{'rolling':>7}  {'':<16}  {r['for']:<6}  {r['verified']:<8}  {r['venue']} — {r['type']}")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    rows = load()
    errors = check(rows)
    if cmd == "check":
        for e in errors:
            print(e)
        print(f"{len(rows)} rows, {len(errors)} errors")
        sys.exit(1 if errors else 0)
    if cmd == "upcoming":
        upcoming(rows)
        return
    raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
