"""
Question 1b: Secure Bank PIN Policy Upgrade

Implements a function to determine minimum changes required to make a PIN strong.
"""
import re

def min_changes_for_strong_pin(pin_code: str) -> int:
    """
    Returns the minimum number of changes required to make the pin_code strong.
    Args:
        pin_code: The PIN string to check.
    Returns:
        Minimum number of changes required.
    """
    n = len(pin_code)
    missing_types = 3 - sum([bool(re.search(r"[a-z]", pin_code)),
                             bool(re.search(r"[A-Z]", pin_code)),
                             bool(re.search(r"[0-9]", pin_code))])
    # Count repeating sequences
    changes = 0
    i = 2
    repeat = 0
    while i < n:
        if pin_code[i] == pin_code[i-1] == pin_code[i-2]:
            repeat += 1
            i += 2
        else:
            i += 1
    if n < 6:
        return max(missing_types, 6-n)
    elif n <= 20:
        return max(missing_types, repeat)
    else:
        # Need to delete extra chars
        delete = n - 20
        changes = delete
        # Reduce repeats with deletions
        changes += max(missing_types, repeat)
        return changes

if __name__ == "__main__":
    print("Example 1:", min_changes_for_strong_pin("X1!"))  # Output: 3
    print("Example 2:", min_changes_for_strong_pin("123456"))  # Output: 2
    print("Example 3:", min_changes_for_strong_pin("Aa1234!"))  # Output: 0
