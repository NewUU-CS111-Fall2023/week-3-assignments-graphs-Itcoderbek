# * Author:Diyorbek Adxamov
# * Date:30.10.2023 
# Task 1
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)] 
forbidden = [list(map(int, input().split())) for i in range(k)]

graph = [[] for i in range(n+1)]
for x, y in edges:
    graph[x].append(y)
    graph[y].append(x)

dist = [-1] * (n+1) 
dist[1] = 0
queue = [1]
while queue:
    u = queue.pop(0)
    for v in graph[u]:
        if dist[v] == -1:
           dist[v] = dist[u] + 1
           queue.append(v)

if dist[n] == -1:
    print(-1)
else:
    print(dist[n])
    path = [n]
    u = n
    while u != 1:
        for v in graph[u]:
            if dist[v] == dist[u] - 1:
                path.append(v)
                u = v
                break
    print(*path[::-1])


# Task 2
import sys
input = sys.stdin.readline

n, m, j = map(int, input().split())
grid = [input() for i in range(n)]

def dfs(i, j, jumps):
    if grid[i][j] == 's':
        if jumps > 0:
            return dfs(i, j, jumps-1)
        else:
            return False
    
    if grid[i][j] == 'x':
        return True
    
    if grid[i][j] == '@':
        return (i, j) == (0, 0)
    
    grid[i][j] = '#'
    
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#':
            if dfs(ni, nj, jumps):
                return True
    
    return False
        
if dfs(0, 0, j):
    print("SUCCESS")
else:
    print("IMPOSSIBLE")
    

# Task 3 
a, b = map(int, input().split())

def transform(a, b):
    q = [(a, 0)]
    visited = set()
    
    while q:
        x, steps = q.pop(0)
        if x == b:
            return steps+1
        if x in visited: 
            continue
            
        visited.add(x)
        q.append((2*x, steps+1)) 
        q.append((10*x + 1, steps+1))
        
    return -1

steps = transform(a, b)

if steps == -1:
    print("NO")
else:
    print("YES")
    print(steps)
    seq = [a]
    for i in range(steps-1):
        if seq[-1] * 2 == b:
            seq.append(seq[-1] * 2)
        else:
            seq.append(10*seq[-1] + 1)
    print(*seq)
    
        
# Task 4
n = int(input())
strs = [input() for i in range(n)]

used = set()
ans = []

def assemble(part):
    if len(part) == len(strs):
        return True
    
    for s in strs:
        if s not in used and s.startswith(part):
            used.add(s)
            if assemble(part + s[len(part):]):
                ans.append(s)
                return True
            used.remove(s)
    return False

assemble("")
print("".join(reversed(ans)))


# Task 5
n, x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dist = [-1] * (n+1)
dist[1] = 0 
queue = [1]
while queue:
    u = queue.pop(0)
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)
            
print(dist[x])
