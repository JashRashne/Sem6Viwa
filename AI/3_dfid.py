def dls(matrix, node, depth, limit, visited):
    if depth > limit or visited[node]:
        return

    print(node, end=" ")
    visited[node] = True

    for i in range(len(matrix)):
        if matrix[node][i] == 1:
            dls(matrix, i, depth+1, limit, visited)

def dfid(matrix, start, max_depth):
    for d in range(max_depth+1):
        print("\nDepth:", d)
        visited = [False]*len(matrix)
        dls(matrix, start, 0, d, visited)

n = int(input("Nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Start: "))
max_depth = int(input("Max depth: "))

dfid(matrix, start, max_depth)
