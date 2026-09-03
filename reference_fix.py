"""
reference_fix.py — YOUR correct version of the function.

Purpose:
  1. Proves the task is actually solvable.
  2. Lets you test your verifier: your verifier run against THIS should PASS.

This is for your eyes only — it must NOT go into the agent's sandbox.

implement `add` correctly, exactly matching the spec in task.md.
"""


def add(numbers: str) -> int:
    if not numbers:
        return 0

    values = numbers.split(",")

    total = 0
    for value in values:
        total += int(value.strip())

    return total


if __name__ == "__main__":
    print(add(""))        # expect 0
    print(add("1"))       # expect 1
    print(add("1,2,3"))   # expect 6
    print(add("1,-2,3"))  # expect 2
    print(add("1, 2 ,3")) # expect 6
