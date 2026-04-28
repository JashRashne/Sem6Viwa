from collections import deque

def bfs(matrix, start):
    visited = [False]*len(matrix)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for i in range(len(matrix)):
            if matrix[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input("Nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Start: "))
bfs(matrix, start)
