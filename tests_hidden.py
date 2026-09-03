"""
tests_hidden.py — the HIDDEN test cases your verifier will use.

This is your "couldn't-memorize" defense (the equivalent of the log task's
secret seed). These cases must NOT be visible to the agent — they do not go
into the Docker sandbox. The agent only sees task.md, not these exact inputs.

Design goal: include cases that a LAZY or HARDCODING fix would get wrong, so
only a REAL fix passes. Cover edge cases, and include a few inputs that are
NOT the same as the examples in task.md (so "hardcode the examples" fails).

Format: a list of (input_string, expected_int) pairs. Keep expected values as
real ints.

TODO: fill in a strong set of cases. Suggestions to get you started below —
add more, especially "surprising" inputs the agent never saw in task.md.
"""

# TODO: expand this. The examples from task.md are a MINIMUM, not enough on
# their own (a hardcoder could pass those). Add fresh, hidden inputs.
CASES = [
    # from the spec (visible to agent) — keep, but don't rely on only these:
    ("", 0),
    ("1", 1),
    ("1,2,3", 6),
    ("1,-2,3", 2),
    ("1, 2 ,3", 6),

    # TODO: add HIDDEN cases the agent never saw, e.g.:
    # ("10,20,30", 60),
    # ("-5,-5", -10),
    # ("  7  ", 7),
    # ("100", 100),
    # ... invent several more, including edge cases you decided on in task.md
]
