# Failure Analysis (fill this in as you attack your own grader)

The point of this file: prove your grader can't be gamed by ACTIVELY trying to
cheat it, and honestly recording what happened.

For each cheat below, create a fake/broken `stringcalc.py`, run your verifier on
it, and record the result. Every one should FAIL (exit 1) with a clear message.

## Attacks to try

| # | Cheat | How to simulate it | Grader result (fill in) |
|---|-------|--------------------|--------------------------|
| 1 | Hardcode the visible examples | `add` uses `if numbers=="1,2,3": return 6` etc., no real logic | TODO |
| 2 | Wrong return type | make `add` return a string like `"6"` | TODO |
| 3 | Returns None / crashes on edge case | `add("")` throws or returns None | TODO |
| 4 | Rename the function | rename `add` to `sum_numbers` | TODO |
| 5 | Empty / deleted file | blank stringcalc.py, or delete it | TODO |
| 6 | (your own idea) | ... | TODO |

## What I learned / what my grader still can't catch

<!-- Be honest here. If an attack slipped through, that's the most valuable
     finding — write what it was and how you'd fix it. -->
TODO

## The key defense in this environment

<!-- One paragraph: explain WHY hidden tests (inputs the agent never saw) are the
     core anti-cheat here, the same principle as the log task's secret seed. -->
TODO
