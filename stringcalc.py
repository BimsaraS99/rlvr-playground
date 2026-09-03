"""
stringcalc.py — buggy starting code the agent must fix.
Bug: missing the empty-string guard, so add("") crashes.
"""


def add(numbers: str) -> int:
    
    values = numbers.split(",")
    total = 0
    for value in values:
        total += int(value.strip())
    return total