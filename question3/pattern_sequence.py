"""
Question 3a: Pattern Sequence Extraction

Given two patterns and repeat counts, find the maximum number of times the second pattern can be formed as a subsequence from the repeated first pattern.
"""
def max_pattern_extraction(p1: str, t1: int, p2: str, t2: int) -> int:
    """
    Returns the maximum number of times p2 can be formed as a subsequence from p1 repeated t1 times, divided by t2.
    Args:
        p1: Base pattern for sequence A.
        t1: Number of times p1 is repeated.
        p2: Base pattern for sequence B.
        t2: Number of times p2 is repeated.
    Returns:
        Maximum x such that p2 * t2 can be extracted from p1 * t1.
    """
    seqA = p1 * t1
    seqB = p2 * t2
    idxA = idxB = count = 0
    while idxA < len(seqA) and idxB < len(seqB):
        if seqA[idxA] == seqB[idxB]:
            idxB += 1
        idxA += 1
        if idxB == len(seqB):
            count += 1
            idxB = 0
    return count

if __name__ == "__main__":
    # Example from assignment
    print("Example:", max_pattern_extraction("bca", 6, "ba", 3))  # Output: 3
