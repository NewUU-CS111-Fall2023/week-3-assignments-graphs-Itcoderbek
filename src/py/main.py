# * Author:Diyorbek Adxamov
# * Date:30.10.2023 task 4 and task5
#task 4
from collections import deque


def numIslands(grid):
    if not grid:
        return 0

    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] != "1":
            return

        grid[row][col] = "#"

        # Explore the neighbors
        dfs(row - 1, col)  # Up
        dfs(row + 1, col)  # Down
        dfs(row, col - 1)  # Left
        dfs(row, col + 1)  # Right

    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "1":
                num_islands += 1
                dfs(i, j)

    return num_islands


def dijkstra_shortest_paths(graph, source):
    num_vertices = len(graph)
    distances = [float("inf")] * num_vertices
    distances[source] = 0
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the minimum distance value
        min_distance = float("inf")
        min_vertex = -1

        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_vertex = v

        visited[min_vertex] = True

        # Update distances of the adjacent vertices
        for neighbor, weight in graph[min_vertex]:
            if not visited[neighbor] and distances[min_vertex] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_vertex] + weight

    return distances


# Example usage for finding the number of islands
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
islands = numIslands(grid)
print(f"Number of islands: {islands}")

#Task 5: Example usage for finding shortest paths using Dijkstra's Algorithm
graph = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    [(4, 3)],
    [(2, 3)],
]
source_vertex = 0
distances = dijkstra_shortest_paths(graph, source_vertex)
print("Shortest distances from the source vertex:")
for i, distance in enumerate(distances):
    print(f"To vertex {i}: {distance}")
