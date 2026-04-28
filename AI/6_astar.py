👉 Here matrix stores cost instead of 0/1
(0 = no edge)

import heapq

n = int(input("Nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

heuristic = list(map(int, input("Heuristic: ").split()))

start = int(input("Start: "))
goal = int(input("Goal: "))

visited = [False]*n
pq = [(heuristic[start], 0, start)]

while pq:
    f, g, node = heapq.heappop(pq)

    if visited[node]:
        continue

    print(node, end=" ")
    visited[node] = True

    if node == goal:
        break

    for i in range(n):
        if matrix[node][i] > 0 and not visited[i]:
            cost = matrix[node][i]
            heapq.heappush(pq, (g + cost + heuristic[i], g + cost, i))
