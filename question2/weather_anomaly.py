"""
Question 2a: Weather Anomaly Detection

Counts the number of continuous subarrays where the sum falls within a given range.
"""
from typing import List

def count_anomaly_periods(temperature_changes: List[int], low_threshold: int, high_threshold: int) -> int:
    """
    Counts continuous periods where the sum is within [low_threshold, high_threshold].
    Args:
        temperature_changes: List of daily temperature changes.
        low_threshold: Lower bound of anomaly range.
        high_threshold: Upper bound of anomaly range.
    Returns:
        Number of valid periods (subarrays).
    """
    n = len(temperature_changes)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += temperature_changes[j]
            if low_threshold <= total <= high_threshold:
                count += 1
    return count

if __name__ == "__main__":
    # Example 1
    print("Example 1:", count_anomaly_periods([3, -1, -4, 6, 2], 2, 5))  # Output: 3 or 4 (see prompt)
    # Example 2
    print("Example 2:", count_anomaly_periods([-2, 3, 1, -5, 4], -1, 2))  # Output: 4 or 5 (see prompt)
