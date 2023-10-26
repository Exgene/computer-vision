import numpy as np
queue = []
visited = np.zeros(20, dtype=int)
adj = np.zeros((20, 20), dtype=int)
n = int(input("Enter verticies"))


def bfs(v: int):
    for i in range(1, n+1):
        if (adj[v][i] and not visited[i]):
            queue.append(i)

    if (len(queue) != 0):
        f = queue.pop(0)
        visited[f] = 1
        bfs(f)


for i in range(1, n+1):
    for j in range(1, n+1):
        adj[i][j] = int(input())

v = int(input("Enter the starting Vertex:"))
bfs(v)

for i in range(1, n+1):
    if visited[i]:
        print(i, "\t")
    else:
        print("Not reachanble for", i)
