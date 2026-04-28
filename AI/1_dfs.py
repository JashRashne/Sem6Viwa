def dfs(matrix, node, visited):
    print(node, end=" ")
    visited[node] = True

    for i in range(len(matrix)):
        if matrix[node][i] == 1 and not visited[i]:
            dfs(matrix, i, visited)

n = int(input("Enter number of nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Start node: "))

visited = [False]*n
dfs(matrix, start, visited)
