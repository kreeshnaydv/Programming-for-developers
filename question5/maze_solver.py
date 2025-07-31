"""
Question 5a: Maze Solver with GUI

A grid-based maze solver supporting DFS and BFS, with random maze generation and visual path animation.
"""
import tkinter as tk
import random
from collections import deque

CELL_SIZE = 30
GRID_SIZE = 15

class MazeSolverGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Maze Solver")
        self.canvas = tk.Canvas(master, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE)
        self.canvas.pack()
        self.reset_maze()
        self.start = (0, 0)
        self.end = (GRID_SIZE-1, GRID_SIZE-1)
        self.draw_maze()

        btn_frame = tk.Frame(master)
        btn_frame.pack()
        tk.Button(btn_frame, text="Solve DFS", command=self.solve_dfs).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Solve BFS", command=self.solve_bfs).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Generate New Maze", command=self.reset_and_draw).pack(side=tk.LEFT)

    def reset_maze(self):
        self.maze = [[1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.generate_maze()

    def reset_and_draw(self):
        self.reset_maze()
        self.start = (0, 0)
        self.end = (GRID_SIZE-1, GRID_SIZE-1)
        self.draw_maze()

    def generate_maze(self):
        # Recursive Backtracking
        stack = [(0, 0)]
        self.maze[0][0] = 0
        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.maze[nx][ny] == 1:
                    neighbors.append((nx, ny))
            if neighbors:
                nx, ny = random.choice(neighbors)
                self.maze[(x+nx)//2][(y+ny)//2] = 0
                self.maze[nx][ny] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

    def draw_maze(self, path=None):
        self.canvas.delete("all")
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = "black" if self.maze[i][j] else "white"
                self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill=color)
        # Draw start and end
        self.canvas.create_rectangle(self.start[1]*CELL_SIZE, self.start[0]*CELL_SIZE, (self.start[1]+1)*CELL_SIZE, (self.start[0]+1)*CELL_SIZE, fill="green")
        self.canvas.create_rectangle(self.end[1]*CELL_SIZE, self.end[0]*CELL_SIZE, (self.end[1]+1)*CELL_SIZE, (self.end[0]+1)*CELL_SIZE, fill="red")
        # Draw path if exists
        if path:
            for (i, j) in path:
                self.canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill="yellow")
        self.master.update()

    def solve_dfs(self):
        path = self.dfs(self.start, self.end)
        self.draw_maze(path)
        self.show_result(path)

    def solve_bfs(self):
        path = self.bfs(self.start, self.end)
        self.draw_maze(path)
        self.show_result(path)

    def show_result(self, path):
        if path:
            tk.messagebox.showinfo("Maze Solver", f"Path found! Steps: {len(path)}")
        else:
            tk.messagebox.showinfo("Maze Solver", "No path found.")

    def dfs(self, start, end):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (x, y), path = stack.pop()
            if (x, y) == end:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.maze[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)]))
        return None

    def bfs(self, start, end):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            (x, y), path = queue.popleft()
            if (x, y) == end:
                return path
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and self.maze[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append(((nx, ny), path + [(nx, ny)]))
        return None

if __name__ == "__main__":
    import tkinter.messagebox
    root = tk.Tk()
    app = MazeSolverGUI(root)
    root.mainloop()
