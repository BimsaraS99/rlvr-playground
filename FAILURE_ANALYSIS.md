# Failure Analysis

The goal of this document is to demonstrate that the grader (`verifier.py`) is
not just correct on honest solutions, but resistant to being *gamed*. To show
this, I took the role of a lazy or sneaky agent and actively attacked my own
grader. For each attack I wrote a cheating `stringcalc.py`, ran the verifier, and
recorded the result. Every attack was caught.

## Attacks tried and results

| # | Cheat | How it tries to game the grader | Grader result |
|---|-------|--------------------------------|---------------|
| 1 | Hardcode the examples | Memorize the 5 visible examples from `task.md` in a dict, with no real logic | **FAIL** — a hidden input (`"10,20,30"`) that the agent never saw is not in the dict, causing a `KeyError`, which `check_one` catches as a failure |
| 2 | Wrong return type | Return the string `"6"` instead of the integer `6` | **FAIL** — the `isinstance(result, int)` check rejects a `str` |
| 3 | Bool trick | Return `True` (in Python `True == 1`, so a naive value-only check would wrongly pass) | **FAIL** — the `isinstance(result, bool)` check runs *before* the int/value checks, so `True` is rejected |
| 4 | Rename the function | Rename `add` to `sum_numbers`, so there is no `add` | **FAIL** — the loader's `callable` guard catches the missing function before any test runs |
| 5 | Delete the file | Remove `stringcalc.py` entirely | **FAIL** — the `os.path.exists` guard reports "File not found" cleanly instead of crashing |

All five attacks resulted in a clean `FAIL` (exit code 1) with a specific message
naming what went wrong. No attack produced a false `PASS`, and no attack crashed
the grader itself.

## The key defense in this environment

The single most important defense is **hidden test inputs**. The agent only sees
the examples written in `task.md`. The verifier, however, grades against a much
larger set of cases in `tests_hidden.py` — including many inputs the agent never
saw. Because of this, the only reliable way to pass is to *actually implement the
logic*; memorizing or hardcoding the visible examples fails the moment a hidden
input is tested (see Attack #1).

This is the same principle as the "secret seed" in my earlier log-analyzer
environment: **grade against something the agent could not have memorized.** In
the log task that took the form of regenerating the input with a seed the agent
never saw; here it takes the form of hidden test cases. Different mechanism, same
core idea — and that idea is what makes the grader ungameable.

The secondary defenses are the layered checks that assume nothing about the
agent's output: load-time guards (file exists, imports cleanly, `add` is present
and callable, correct signature), and per-result guards (no exceptions, not a
bool, is an int, correct value). Each guard closes one specific way the agent
could otherwise slip a bad answer past the grader.

## Honest limitations (what a stronger version would still need)

Being honest about what this grader does *not* yet handle:

1. **Inaccurate message for a missing function.** When `add` is missing entirely,
   the grader prints `"'add' exists but is not callable"`, which is misleading —
   in that case `add` does not exist at all. The check is correct (it fails), but
   the wording should distinguish "no `add` found" from "`add` is present but not
   a function." An easy fix: check `hasattr(module, "add")` separately and give a
   distinct message.

2. **No sandboxing or timeout — the biggest gap.** The verifier runs the agent's
   code *directly* on the host machine. A malicious agent could do real damage
   (delete files, exfiltrate data) and a buggy one could loop forever or exhaust
   memory, hanging the grader. A production version must run the agent's code
   inside an isolated container (Docker) with strict CPU/memory/time limits and no
   network access. This is exactly what the `Dockerfile` in this project is for:
   it provides a disposable, sealed sandbox that (a) protects the host from
   untrusted code, (b) can enforce resource limits, and (c) contains only
   `task.md` and `stringcalc.py`, so the agent physically cannot read the hidden
   tests or the grader to cheat.

3. **Single fixed task.** This environment grades one task. A real training
   environment would generate many task variants so an agent cannot overfit to a
   single problem. The seedable-generation idea from the log-analyzer environment
   would extend this naturally.

4. **Spec/test coupling is manual.** I had to manually keep `task.md` and
   `tests_hidden.py` in agreement (e.g. when I added `+` and tab handling). A
   larger environment would benefit from generating tests from a single source of
   truth to avoid drift between what the agent is told and what is tested.