import heapq

n = int(input("Nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

heuristic = list(map(int, input("Heuristic values: ").split()))

start = int(input("Start: "))
goal = int(input("Goal: "))

visited = [False]*n
pq = [(heuristic[start], start)]

while pq:
    _, node = heapq.heappop(pq)

    if visited[node]:
        continue

    print(node, end=" ")
    visited[node] = True

    if node == goal:
        break

    for i in range(n):
        if matrix[node][i] == 1 and not visited[i]:
            heapq.heappush(pq, (heuristic[i], i))
