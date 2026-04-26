def dls(node, visited, graph, limit, depth, traversal, call_counter):
    call_counter[0] += 1  # count recursive calls

    if depth > limit:
        return

    visited[node] = True
    traversal.append(node)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dls(neighbor, visited, graph, limit, depth + 1, traversal, call_counter)


# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Graph (adjacency list)
graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # remove if directed

# Inputs for DLS
start_node = int(input("Enter starting node: "))
limit = int(input("Enter depth limit: "))

visited = [False] * n
traversal = []
call_counter = [0]

# Run DLS
dls(start_node, visited, graph, limit, 0, traversal, call_counter)

# Output
print("DLS Traversal (limit =", limit, "):", traversal)
print("Number of recursive calls:", call_counter[0])






"""
Enter number of nodes: 5
Enter number of edges: 4
Enter edges (u v):
0 1
0 2
1 3
1 4
Enter starting node: 0
Enter depth limit: 1
"""