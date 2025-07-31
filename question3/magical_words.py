"""
Question 3b: Magical Words (Odd-length Palindromes)

Find two non-overlapping magical words (odd-length palindromes) in a string to maximize the product of their lengths.
"""
def max_magical_power(M: str) -> int:
    """
    Returns the maximum product of lengths of two non-overlapping odd-length palindromic substrings.
    Args:
        M: The manuscript string.
    Returns:
        Maximum product of lengths.
    """
    n = len(M)
    # Find all odd-length palindromes
    palindromes = []  # (start, end, length)
    for center in range(n):
        l = r = center
        while l >= 0 and r < n and M[l] == M[r]:
            if (r - l + 1) % 2 == 1:
                palindromes.append((l, r, r - l + 1))
            l -= 1
            r += 1
    # Try all pairs of non-overlapping palindromes
    max_product = 0
    for i in range(len(palindromes)):
        for j in range(i + 1, len(palindromes)):
            a = palindromes[i]
            b = palindromes[j]
            # Check non-overlapping
            if a[1] < b[0] or b[1] < a[0]:
                max_product = max(max_product, a[2] * b[2])
    return max_product

if __name__ == "__main__":
    # Example 1
    print("Example 1:", max_magical_power("xyzyxabc"))  # Output: 5
    # Example 2
    print("Example 2:", max_magical_power("levelwowracecar"))  # Output: 35
