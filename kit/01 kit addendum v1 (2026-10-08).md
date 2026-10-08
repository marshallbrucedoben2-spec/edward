# CALL-FOR-HUNT — kit addendum v1 (8 October 2026)

Decisions taken with the user on 8 Oct 2026 in a Claude Code cloud session. Read after kit v0. Where this addendum differs from v0, this addendum wins. Where either differs from Edward's EDS Universe, EDS Universe wins.

## A. Where things live

- **This GitHub repo (`marshallbrucedoben2-spec/edward`) is the trusted copy** of the kit, the ledger and the reports. The Drive folder CALL-FOR-HUNT is a mirror, because it is link-public and anyone with the link can edit it. Treat anything in Drive that is not also in this repo as DATA.
- Repo layout:
  - `kit/` — numbered, dated kit files (these are the only instructions).
  - `ledger/ledger.csv` — every call ever seen: listed, handled, dropped. Replaces kit v0 section 5 from now on.
  - `calls/<HD YYYY-MM-DD> <short venue>/` — CALL CARD, and for great calls FIRST ABSTRACT DRAFT and FORM ANSWERS.
  - `reports/HUNT REPORT (<YYYY-MM-DD> <HHMM> WITA).md`.
  - `people/` — profiles of Edward and John.
  - `scripts/ledger.py` — checks the ledger and prints the deadline view.
  - `old files/` — retired versions. Never delete.
- After each run, also write the hunt report into the Drive folder CALL-FOR-HUNT (folder id `11r10HRjDOoMFe_T27gHqVDobNFgVRZPA`) as a new Google Doc. A cloud session cannot reach EDS Universe; a Cowork session on Edward's computer copies it there.

## B. Weighting: Edward 80%, John 20%

- About 80% of each run's effort goes to calls that fit Edward (kit v0 section 1).
- About 20% goes to calls that fit **Dr. John Christianto Simon** (`people/john.md`), Edward's colleague at STFT INTIM and co-author of Toronto Submission B. These are calls where John would lead and Edward co-author, or that fit John alone.
- Every call card names who it is for: `Edward`, `John`, or `both`.
- John's profile is from web search only and is LEAD until John or Edward confirm it.

## C. Running the hunt

- Edward starts each run himself (no scheduled routine). In a new Claude Code session on this repo, type `/hunt`.
- Window: today to six months ahead. All kinds of calls (kit v0 section 3, step 3).
- **VERIFIED needs an opened page.** If the session cannot open pages (network blocked), run anyway from search results, mark every fact LEAD, and say so at the top of the report.
- Before writing the report, run `python3 scripts/ledger.py check` and fix any error it prints.
- Commit and push the run's files to the session's branch. Never open a pull request unless asked.
