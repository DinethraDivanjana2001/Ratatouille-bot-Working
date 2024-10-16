import tkinter as tk
from collections import deque
import os

# Define the 31x31 maze and initialize the flood fill values
#maze_discovered.text has line by line space separates 31x 31 maze
script_dir = os.path.dirname(__file__)  # Get the directory of the script
file_path = os.path.join(script_dir, "maze_discovered.txt")

maze = []
with open(file_path, "r") as f:
    for line in f:
        maze.append(list(map(int, line.split())))

print(maze)

flood_fill = [[-1 for _ in range(31)] for _ in range(31)]

# Flood fill algorithm
def flood_fill_algorithm(maze, flood_fill, start):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    flood_fill[start[0]][start[1]] = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        current_distance = flood_fill[x][y]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and flood_fill[nx][ny] == -1:
                flood_fill[nx][ny] = current_distance + 1
                queue.append((nx, ny))

goal = (30, 0)
flood_fill_algorithm(maze, flood_fill, goal)

# Visualization with tkinter
def draw_grid(canvas, maze, flood_fill):
    global goal

    cell_size = 20
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            
            if maze[i][j] == 1:
                color = "black"
            else:
                if flood_fill[i][j] == -1:
                    color = "white"
                else:
                    temp = (hex((255 - flood_fill[i][j])*5)[-2:])[-2:]
                    color = f"#{temp}ff00"

            if i == goal[0] and j == goal[1]:
                color = "red"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
            canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text=flood_fill[i][j], fill="black")
            

# Main tkinter window
root = tk.Tk()
root.title("Micromouse Flood Fill Visualization")

canvas = tk.Canvas(root, width=620, height=620)
canvas.pack()

draw_grid(canvas, maze, flood_fill)

root.mainloop()
