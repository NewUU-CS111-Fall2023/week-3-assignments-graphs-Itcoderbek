/*
 * Author:Diyorbek
 * Date:30.102023
 * Name:task 1,2,3
 */

#include <iostream>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

// Task 1: Depth First Search (DFS) for a Graph

class Graph {
    int numVertices;
    vector<vector<int>> adjList;

public:
    Graph(int V) {
        numVertices = V;
        adjList.resize(V);
    }

    void addEdge(int u, int v) {
        adjList[u].push_back(v);
    }

    void DFSUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";

        for (int i : adjList[v]) {
            if (!visited[i]) {
                DFSUtil(i, visited);
            }
        }
    }

    void DFS(int v) {
        vector<bool> visited(numVertices, false);
        DFSUtil(v, visited);
    }
};

// Task 2: Shortest path in a Binary Maze

struct Point {
    int x, y;
};

bool isValid(int row, int col, int numRows, int numCols) {
    return (row >= 0 && row < numRows && col >= 0 && col < numCols);
}

int shortestPathBinaryMaze(vector<vector<int>>& maze, Point src, Point dest) {
    int numRows = maze.size();
    int numCols = maze[0].size();

    if (maze[src.x][src.y] == 0 || maze[dest.x][dest.y] == 0) {
        return -1; // Invalid source or destination
    }

    vector<vector<bool>> visited(numRows, vector<bool>(numCols, false));

    int dx[] = {-1, 0, 1, 0}; // Possible movements: up, right, down, left
    int dy[] = {0, 1, 0, -1};

    queue<pair<Point, int>> q;
    q.push(make_pair(src, 0));
    visited[src.x][src.y] = true;

    while (!q.empty()) {
        pair<Point, int> front = q.front();
        Point curr = front.first;
        int dist = front.second;
        q.pop();

        if (curr.x == dest.x && curr.y == dest.y) {
            return dist; // Shortest path found
        }

        for (int i = 0; i < 4; i++) {
            int newRow = curr.x + dx[i];
            int newCol = curr.y + dy[i];

            if (isValid(newRow, newCol, numRows, numCols) && maze[newRow][newCol] && !visited[newRow][newCol]) {
                visited[newRow][newCol] = true;
                q.push(make_pair(Point{newRow, newCol}, dist + 1));
            }
        }
    }

    return -1; // No path found
}

// Task 3: Print all paths from a given source to a destination

void printAllPathsUtil(vector<vector<int>>& graph, int v, int d, vector<int>& path, vector<bool>& visited) {
    visited[v] = true;
    path.push_back(v);

    if (v == d) {
        for (int i : path) {
            cout << i << " ";
        }
        cout << endl;
    } else {
        for (int i : graph[v]) {
            if (!visited[i]) {
                printAllPathsUtil(graph, i, d, path, visited);
            }
        }
    }

    visited[v] = false;
    path.pop_back();
}

void printAllPaths(vector<vector<int>>& graph, int s, int d) {
    int numVertices = graph.size();
    vector<bool> visited(numVertices, false);
    vector<int> path;

    printAllPathsUtil(graph, s, d, path, visited);
}

int main() {
    // Task 1: Depth First Search (DFS) for a Graph
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "DFS traversal starting from vertex 2: ";
    g.DFS(2);
    cout << endl;

    // Task 2: Shortest path in a Binary Maze
    vector<vector<int>> maze = {
        {1, 0, 1, 1, 1},
        {1, 0, 1, 0, 1},
        {1, 1, 1, 0, 1},
        {0, 0, 1, 0, 1},
        {0, 0, 1, 1, 1}
    };

    Point src = {0, 0};
    Point dest = {4, 4};

    int shortestPath = shortestPathBinaryMaze(maze, src, dest);
    if (shortestPath != -1) {
        cout << "Shortest path length from source to destination: " << shortestPath << endl;
    } else {
        cout << "No path found from source to destination." << endl;
    }

    // Task 3: Print all paths from a given source to a destination
    vector<vector<int>> graph = {
        {1, 2},
        {2},
        {3},
        {0, 1}
    };

    int source = 2;
    int destination = 3;

    cout << "All paths from source " << source << " to destination " << destination << ":\n";
    printAllPaths(graph, source, destination);

    return 0;
}
