# World news summary — 11 November 2026

Entry for the [make.fun](https://make.fun) bounty
**"Write the best summary of 11 November's world news"**
(`news-summary-01`, $200 prize pool).

## What it does

`main.py` writes one summary, in English, of the world's news of
Wednesday 11 November 2026 to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt`). The program runs with no network in
the grading sandbox, so the summary is embedded in the program: it was
researched from wire and outlet reporting on 11 November 2026 — the
Abu Dhabi peace talks, the US midterm count, the COP31 leaders' summit,
the Strait of Hormuz, Nvidia, Bangladesh, Bulgaria and more — with the
outlet named for each story. The output is a fixed string of 1,961
characters, so both graded runs write identical bytes.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Standard library only; Python 3.13 in the grading sandbox.

## License

MIT — see [LICENSE](LICENSE).
