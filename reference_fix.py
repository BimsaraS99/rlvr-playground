"""
reference_fix.py — YOUR correct version of the function.

Purpose:
  1. Proves the task is actually solvable.
  2. Lets you test your verifier: your verifier run against THIS should PASS.

This is for your eyes only — it must NOT go into the agent's sandbox.

TODO: implement `add` correctly, exactly matching the spec in task.md.
"""


def add(numbers: str) -> int:
    # TODO: implement the correct behavior:
    #   ""        -> 0
    #   "1"       -> 1
    #   "1,2,3"   -> 6
    #   "1,-2,3"  -> 2
    #   "1, 2 ,3" -> 6
    #   (plus any extra rules you added to task.md)
    raise NotImplementedError("write the correct version here")


if __name__ == "__main__":
    # Quick self-test so you can eyeball it before wiring up the verifier.
    print(add(""))        # expect 0
    print(add("1"))       # expect 1
    print(add("1,2,3"))   # expect 6
    print(add("1,-2,3"))  # expect 2
    print(add("1, 2 ,3")) # expect 6
