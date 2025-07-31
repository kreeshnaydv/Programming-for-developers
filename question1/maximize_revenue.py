"""
Question 1a: Maximizing Tech Startup Revenue before Acquisition

Implements a function to determine the maximum possible capital after at most k projects.
"""
from typing import List
import heapq

def maximize_capital(k: int, c: int, revenues: List[int], investments: List[int]) -> int:
    """
    Selects up to k projects to maximize final capital, given initial capital c.
    Args:
        k: Maximum number of projects.
        c: Initial capital.
        revenues: List of revenue gains for each project.
        investments: List of required capital for each project.
    Returns:
        Maximum capital after up to k projects.
    """
    n = len(revenues)
    projects = sorted(zip(investments, revenues), key=lambda x: x[0])
    max_heap = []  # max-heap for available projects (by revenue)
    i = 0
    capital = c

    for _ in range(k):
        # Add all projects that can be started with current capital
        while i < n and projects[i][0] <= capital:
            heapq.heappush(max_heap, -projects[i][1])  # Use negative for max-heap
            i += 1
        if not max_heap:
            break
        # Select the project with the highest revenue
        capital += -heapq.heappop(max_heap)
    return capital

if __name__ == "__main__":
    # Example 1
    print("Example 1:", maximize_capital(2, 0, [2, 5, 8], [0, 2, 3]))  # Output: 7
    # Example 2
    print("Example 2:", maximize_capital(3, 1, [3, 6, 10], [1, 3, 5]))  # Output: 19
