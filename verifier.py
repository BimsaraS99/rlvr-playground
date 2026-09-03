"""
verifier.py — THE GRADER (your main deliverable).

Goal: decide PASS/FAIL for the agent's fixed stringcalc.py by RUNNING it against
your hidden tests — and resist every cheat you can think of.

Your verifier must:
  1. Safely load the agent's stringcalc.py (fail cleanly if missing / has syntax
     errors / no `add` function / wrong signature).
  2. Run every case in tests_hidden.CASES against the agent's `add`.
  3. For each case: catch exceptions (a crash = fail, not a grader crash), and
     check the return is the RIGHT TYPE (int, not str, not bool) AND the right value.
  4. Print PASS only if ALL cases pass; otherwise print FAIL naming the first
     failing case (input, expected, got).
  5. Exit 0 on pass, 1 on fail.

Think adversarially as you write each check. For every line, ask:
  "How would a lazy/sneaky model make this pass without really fixing the code?"
and close that door. See task2-brief.md for the 5 cheats to defend against.

Below is a SKELETON with TODOs. Fill it in yourself.
"""

import sys
import importlib.util

from tests_hidden import CASES


def fail(msg: str):
    """Print a clear failure reason and exit 1."""
    print(f"FAIL: {msg}")
    sys.exit(1)


def load_agent_add(path: str = "stringcalc.py"):
    """
    Load the agent's module from `path` and return its `add` function.
  
    TODO:
      - Handle: file missing -> fail(...)
      - Handle: import/syntax error -> fail(...)  (use try/except around exec_module)
      - Handle: no `add` attribute -> fail(...)
      - (Optional) check it's callable / signature looks right -> fail(...)
    Return the `add` function if all good.
    """
    # HINT (loading a module from a file path):
    #   spec = importlib.util.spec_from_file_location("agent_stringcalc", path)
    #   module = importlib.util.module_from_spec(spec)
    #   spec.loader.exec_module(module)   # <- can raise; wrap in try/except
    #   return module.add

    # Guard 1 (missing file)
    import os
    if not os.path.exists(path):
        fail(f"File not found: {path}")

    # Guard 2 (syntax / import error)
    spec = importlib.util.spec_from_file_location("agent_stringcalc", path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)   # runs the agent's file; can raise
    except Exception as e:
        fail(f"could not import {path}: {e}")

    # Guard 3 (no `add` attribute)
    add_fn = getattr(module, "add", None)
    if not callable(add_fn):
        fail("'add' exists but is not callable")

    # Guard 4 (optional: check it's callable / signature looks right)
    import inspect
    sig = inspect.signature(add_fn)
    if len(sig.parameters) != 1:
        fail(f"'add' has wrong number of parameters: {len(sig.parameters)}")

    return add_fn


def check_one(add_fn, text, expected):
    """
    Run add_fn(text) and return (ok: bool, detail: str).

      - call add_fn(text) inside try/except; an exception => not ok
      - reject bool results (in Python True == 1, sneaky!) => not ok
      - require isinstance(result, int) => else not ok
      - compare result == expected
    """

    # call it, catching any exception as a failure
    try:
        result = add_fn(text)
    except Exception as e:
        return False, f"raised {type(e).__name__}: {e}"

    # reject bool results (True == 1, sneaky!)
    if isinstance(result, bool):
        return False, f"returned bool {result} (not int)"

    # require isinstance(result, int)
    if not isinstance(result, int):
        return False, f"returned {type(result).__name__} (not int)"

    # compare result == expected
    if result != expected:
        return False, f"expected {expected}, got {result}"

    return True, "PASS"


def main():
    add_fn = load_agent_add("stringcalc.py")

    for text, expected in CASES:
        ok, detail = check_one(add_fn, text, expected)
        if not ok:
            # report WHICH input failed, plus the detail from check_one
            fail(f"input {text!r}: {detail}")

    # if we get here, every case passed
    print("PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()
