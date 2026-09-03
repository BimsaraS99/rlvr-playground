# Task: Fix the broken string calculator

<!--
TODO (you, the environment engineer): write the prompt the AGENT will read.
This is the spec. Make it PRECISE — every rule the tests check must be stated
here, and nothing ambiguous. Below is a starting point; edit it to match the
exact behavior your hidden tests will enforce.
-->

You are in a Linux environment. The current directory contains a file
`stringcalc.py` with a function `add` that has bugs.

Fix `stringcalc.py` so that `add(numbers: str) -> int` behaves exactly as
specified:

- `add("")` returns `0`
- `add("1")` returns `1`
- `add("1,2,3")` returns `6`
- Negative numbers are allowed: `add("1,-2,3")` returns `2`
- Spaces around numbers are ignored: `add("1, 2 ,3")` returns `6`

<!-- TODO: decide and STATE any extra rules your tests will check, e.g.:
     - what about a trailing comma "1,2,"?
     - what about a single space " "?
     Whatever your hidden tests check, the rule MUST be written here. -->

Requirements:
- Do NOT change the function name or signature (`add(numbers: str) -> int`).
- The function must return an `int`.
- `python -c "import stringcalc"` must succeed (no syntax errors).
