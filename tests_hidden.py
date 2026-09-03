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

Fill in a strong set of cases. Suggestions to get you started below —
add more, especially "surprising" inputs the agent never saw in task.md.
"""

# expand this. The examples from task.md are a MINIMUM, not enough on
# their own (a hardcoder could pass those). Add fresh, hidden inputs.
CASES = [
    # From the spec (visible to agent)
    ("", 0),
    ("1", 1),
    ("1,2,3", 6),
    ("1,-2,3", 2),
    ("1, 2 ,3", 6),

    # Basic hidden cases
    ("10,20,30", 60),
    ("-5,-5", -10),
    ("  7  ", 7),
    ("100", 100),

    # Zero
    ("0", 0),
    ("0,0", 0),
    ("0,0,0", 0),
    ("1,0,2", 3),
    ("-1,0,1", 0),
    ("10,0,-10", 0),

    # Positive numbers
    ("2,4,6", 12),
    ("5,10,15,20", 50),
    ("10,10,10,10", 40),
    ("100,200,300,400", 1000),
    ("1,2,3,4,5,6,7,8,9,10", 55),

    # Negative numbers
    ("-1", -1),
    ("-1,-2,-3", -6),
    ("-10,-20,-30", -60),
    ("-100,-200", -300),
    ("-5,-10,20", 5),
    ("-10,5,3", -2),

    # Mixed positive and negative
    ("5,-3,2,-4,10", 10),
    ("10,-5,3,-2", 6),
    ("100,-50,25,-10", 65),
    ("-100,50,25", -25),
    ("-10,20,-30,40", 20),
    ("50,-25,-25", 0),

    # Whitespace
    (" 1 ", 1),
    ("  10  ", 10),
    (" 1,2,3 ", 6),
    (" 1 , 2 , 3 ", 6),
    ("  10 , 20 , 30  ", 60),
    ("\t5\t", 5),
    ("\t1,\t2,\t3\t", 6),

    # Larger numbers
    ("1000,2000,3000", 6000),
    ("10000,20000", 30000),
    ("100000,200000,300000", 600000),
    ("999999,1", 1000000),
    ("1000000,-500000", 500000),

    # Repeated values
    ("5,5,5", 15),
    ("-2,-2,-2", -6),
    ("100,100,100", 300),
    ("1,1,1,1,1,1,1,1,1,1", 10),

    # Many numbers
    ("1,2,3,4,5,6,7,8,9,10,11,12", 78),
    ("10,20,30,40,50,60,70,80,90,100", 550),
    ("-1,-2,-3,-4,-5,5,4,3,2,1", 0),

    # Single values with whitespace/sign
    ("-10", -10),
    ("+10", 10),
    (" +5 ", 5),
    (" -5 ", -5),
]
