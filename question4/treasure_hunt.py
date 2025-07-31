"""
Question 4b: Treasure Hunt Game (Graph Simulation)

Simulates a two-player treasure hunt game on an undirected graph with draw/win/lose conditions.
"""
from typing import List, Tuple

def treasure_hunt_game(graph: List[List[int]]) -> int:
    """
    Returns 1 if Player 1 wins, 2 if Player 2 wins, 0 for draw.
    Player 1 starts at node 1, Player 2 at node 2, Treasure at node 0.
    Player 2 cannot move to node 0.
    """
    from collections import deque
    N = len(graph)
    # State: (p1_pos, p2_pos, turn)   turn: 1 for Player 1, 2 for Player 2
    visited = set()
    queue = deque()
    queue.append((1, 2, 1))
    while queue:
        p1, p2, turn = queue.popleft()
        if (p1, p2, turn) in visited:
            return 0  # Draw by repetition
        visited.add((p1, p2, turn))
        if p1 == 0:
            return 1  # Player 1 wins
        if p1 == p2:
            return 2  # Player 2 wins
        if turn == 1:
            # Player 1 moves
            for nxt in graph[p1]:
                queue.append((nxt, p2, 2))
        else:
            # Player 2 moves (cannot go to 0)
            for nxt in graph[p2]:
                if nxt != 0:
                    queue.append((p1, nxt, 1))
    return 0  # Draw if queue is exhausted

if __name__ == "__main__":
    Graph = [
        [2, 5],  # Node 0
        [3],     # Node 1
        [0, 4, 5],
        [1, 4, 5],
        [2, 3],
        [0, 2, 3]
    ]
    print("Example:", treasure_hunt_game(Graph))  # Output: 0 (Draw)
