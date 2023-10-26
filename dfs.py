import numpy as np
reach = np.zeros(50)
adj = np.zeros((20, 20))

n = int(input("Enter the No of Vertices!"))


def dfs(v: int):
    reach[v] = 1
    for i in range(1, n+1):
        if (adj[v][i] and reach[i] != 1):
            print(v, " -> ", i)
            dfs(i)


for i in range(1, n+1):
    for j in range(1, n+1):
        reach[i] = 0
        adj[i][j] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        adj[i][j] = int(input())

dfs(1)
count = 0

for i in range(1, n+1):
    if (reach[i] != 0):
        count += 1

if (count == n):
    print("Connected Graph!")
else:
    print("Disconnected Graph!")
