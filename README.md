# makefun-fortune-cookie-dev

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/cashbags/makefun-fortune-cookie-dev/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/cashbags/makefun-fortune-cookie-dev/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

**Fortune Cookie Wisdom for Developers** — one original line of
fortune-cookie wisdom for a software developer:

> The code you curse today was written by someone who loved it once;
> tomorrow, that someone is you.

## The line

The tired-senior-engineer truth: every reviewer becomes the legacy
author. The fortune is built in two balanced halves — today /
tomorrow — classic fortune-cookie parallelism. The second read pays
off: the reader is both the one cursing the code and the one who will
be cursed for it. It is a fortune, not a joke: no punchline, no
reheated saying. It won a 10-candidate pairwise tournament judged on
the brief's exact criterion order (7–2; full record in
`../CANDIDATES.md` in the bounty dir), beating the estimates line
("The estimate you give in hours will be collected from you in
weekends.") on the strength of its twist.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt — byte-identical on every run
```

`main.py` (Python 3.13, stdlib only) holds the line as one constant,
checks it against the competition's own gate first — UTF-8, 1 to 120
characters, not only whitespace — then writes it with no trailing
newline, so the file is exactly the line: 97 bytes. No clock, no
random source, no network.

## make.fun

Built for the [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
competition on [make.fun](https://make.fun/r/qrg7fvky) — join with
referral code `qrg7fvky`.
