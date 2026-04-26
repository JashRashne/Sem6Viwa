def dfs(node, visited, graph, traversal, call_counter):
    call_counter[0] += 1  # count this recursive call
    visited[node] = True
    traversal.append(node)

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph, traversal, call_counter)


# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

# Initialize graph (adjacency list)
graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # remove this line if graph is directed

# DFS execution
visited = [False] * n
traversal = []
call_counter = [0]  # using list to pass by reference

start_node = int(input("Enter starting node for DFS: "))
dfs(start_node, visited, graph, traversal, call_counter)

# Output
print("DFS Traversal:", traversal)
print("Number of recursive calls:", call_counter[0])









"""
Enter number of nodes: 5
Enter number of edges: 4
Enter edges (u v):
0 1
0 2
1 3
1 4
Enter starting node for DFS: 0
"""