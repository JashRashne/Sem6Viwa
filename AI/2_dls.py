def dls(matrix, node, depth, limit):
    if depth > limit:
        return

    print(node, end=" ")

    for i in range(len(matrix)):
        if matrix[node][i] == 1:
            dls(matrix, i, depth+1, limit)

n = int(input("Nodes: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

start = int(input("Start: "))
limit = int(input("Depth limit: "))

dls(matrix, start, 0, limit)
