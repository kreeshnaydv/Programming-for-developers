"""
Question 2b: Alphametic Puzzle Solver

Checks if there is a valid digit assignment for a given word equation.
"""
from typing import List, Dict, Set
import itertools

def word_to_number(word: str, mapping: Dict[str, int]) -> int:
    return int(''.join(str(mapping[ch]) for ch in word))

def is_valid_mapping(words: List[str], result: str, mapping: Dict[str, int]) -> bool:
    # No word can have leading zero
    for w in words + [result]:
        if mapping[w[0]] == 0:
            return False
    total = sum(word_to_number(w, mapping) for w in words)
    return total == word_to_number(result, mapping)

def solve_alphametic(words: List[str], result: str) -> bool:
    """
    Returns True if a valid digit assignment exists, False otherwise.
    Args:
        words: List of words to sum.
        result: The result word.
    Returns:
        True if possible, False otherwise.
    """
    letters = set(''.join(words + [result]))
    if len(letters) > 10:
        return False
    letters = list(letters)
    for perm in itertools.permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if is_valid_mapping(words, result, mapping):
            return True
    return False

if __name__ == "__main__":
    # Example 1: STAR + MOON = NIGHT (should be True for some mapping)
    print("Example 1:", solve_alphametic(["STAR", "MOON"], "NIGHT"))
    # Example 2: CODE + BUG = DEBUG (should be False)
    print("Example 2:", solve_alphametic(["CODE", "BUG"], "DEBUG"))
