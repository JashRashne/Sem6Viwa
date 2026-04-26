from collections import deque

def bfs(start, graph, visited, traversal, visit_counter):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        traversal.append(node)
        visit_counter[0] += 1  # count visits

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


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

start_node = int(input("Enter starting node for BFS: "))

visited = [False] * n
traversal = []
visit_counter = [0]

# Run BFS
bfs(start_node, graph, visited, traversal, visit_counter)

# Output
print("BFS Traversal:", traversal)
print("Number of node visits:", visit_counter[0])








"""
Enter number of nodes: 5
Enter number of edges: 4
Enter edges (u v):
0 1
0 2
1 3
1 4
Enter starting node for BFS: 0
"""