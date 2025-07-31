"""
Question 4a: Secure Transmission

Implements a class to check if a message can be securely transmitted between offices with signal strength limits.
"""
from typing import List
from collections import deque, defaultdict

class SecureTransmission:
    def __init__(self, n: int, links: List[List[int]]):
        """
        Initializes the system with n offices and a list of communication links.
        Args:
            n: Number of offices (nodes).
            links: List of [a, b, strength] edges.
        """
        self.graph = defaultdict(list)
        for a, b, strength in links:
            self.graph[a].append((b, strength))
            self.graph[b].append((a, strength))

    def canTransmit(self, sender: int, receiver: int, maxStrength: int) -> bool:
        """
        Returns True if a path exists between sender and receiver with all links < maxStrength.
        """
        visited = set()
        queue = deque([sender])
        while queue:
            node = queue.popleft()
            if node == receiver:
                return True
            visited.add(node)
            for neighbor, strength in self.graph[node]:
                if neighbor not in visited and strength < maxStrength:
                    queue.append(neighbor)
        return False

if __name__ == "__main__":
    # Example from assignment
    st = SecureTransmission(6, [[0,2,4],[2,3,1],[2,1,3],[4,5,5]])
    print(st.canTransmit(2, 3, 2))  # True
    print(st.canTransmit(1, 3, 3))  # False
    print(st.canTransmit(2, 0, 3))  # True
    print(st.canTransmit(0, 5, 6))  # False
