#!/usr/bin/env python3
"""make.fun bounty entry: news-summary-01.

Writes one summary, in English, of the world's news of Wednesday
11 November 2026 to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The program runs with no network in the grading sandbox, so the summary
is embedded below: it was researched from wire and outlet reporting on
11 November 2026 (AP, Reuters, Arab News, Daily Star, BTA, NY Post).
The output is a fixed string, so both graded runs write identical bytes.
Standard library only.
"""

import os
from pathlib import Path

SUMMARY = """World news \u2014 Wednesday 11 November 2026

Russia and Ukraine held a second day of US-mediated peace talks in Abu Dhabi, their first direct round since February. Day one ran about four hours and ended with no deal and no joint statement; security guarantees came first, territory on day two. Both sides showed some flexibility on land, a US official said. (Reuters, AP)

In Washington, the Democrats' midterm sweep firmed up: the Associated Press put them at 254 House seats to 163, with 16 races uncalled, and at least 54 Senate seats after seven flips. They take both chambers when the new Congress sits in January. (AP)

At the COP31 climate summit in Antalya, T\u00fcrkiye, world leaders began two days of speeches, with about 102 leaders expected. T\u00fcrkiye, hosting for the first time, is pushing an electrification goal; the US stayed away for a second year. (Reuters)

Secretary of State Marco Rubio said there was no need to strike Iran again as diplomacy gathered steam, while Iran's Revolutionary Guard said three oil tankers were on fire in the Strait of Hormuz and the UK maritime agency confirmed a tanker incident. (Arab News)

Nvidia lost nearly $450bn in two days as the FBI examination of chief Jensen Huang continued; three House committee chairs want his reply by Wednesday to a closed-door briefing request for 18 November. (Reuters, NY Post)

In Bangladesh, a shutdown called by the banned Chhatra League brought arson and crude-bomb attacks across the country, killing a bus driver in Faridpur. (Daily Star)

Bulgaria held a day of national mourning after fog caused two pile-ups on the Trakia motorway near Yambol, killing at least 11 people and injuring about 50. (BTA)

A border crossing between Lebanon and Syria reopened after a two-year closure, and in Beirut former Iraqi MP Ahmed al-Alwani was found strangled in his apartment. (Arab News)

It was also Remembrance Day in the Commonwealth, Veterans Day in the US and Singles' Day in China."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(SUMMARY, encoding="utf-8")
    print(f"wrote {target} ({len(SUMMARY)} characters)")


if __name__ == "__main__":
    main()
