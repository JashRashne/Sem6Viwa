def dfid(start, graph, max_depth, n):
    total_calls = 0

    for limit in range(max_depth + 1):
        visited = [False] * n
        traversal = []
        call_counter = [0]

        dls(start, graph, limit, 0, visited, traversal, call_counter)

        total_calls += call_counter[0]

        print(f"Depth {limit}: {traversal} | Calls: {call_counter[0]}")

    print("Total recursive calls:", total_calls)


# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # remove if directed

start_node = int(input("Enter starting node: "))
max_depth = int(input("Enter maximum depth: "))

# Run DFID
dfid(start_node, graph, max_depth, n)


"""
Enter number of nodes: 5
Enter number of edges: 4
Enter edges (u v):
0 1
0 2
1 3
1 4
Enter starting node: 0
Enter maximum depth: 2
"""