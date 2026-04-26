import heapq

def greedy_bfs(start, goal, graph, heuristic):
    visited = set()
    pq = []  # priority queue (min-heap)
    heapq.heappush(pq, (heuristic[start], start))

    traversal = []
    expansions = 0

    while pq:
        h, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        traversal.append(node)
        expansions += 1

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

    return traversal, expansions


# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # remove if directed

# Heuristic input
heuristic = {}
print("Enter heuristic values (node h(n)):")
for _ in range(n):
    node, h = map(int, input().split())
    heuristic[node] = h

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

# Run GBFS
traversal, expansions = greedy_bfs(start, goal, graph, heuristic)

# Output
print("Greedy Best First Traversal:", traversal)
print("Number of node expansions:", expansions)




"""
Enter number of nodes: 5
Enter number of edges: 6
Enter edges (u v):
0 1
0 2
1 3
2 3
3 4
1 4

Enter heuristic values (node h(n)):
0 5
1 3
2 4
3 2
4 0

Enter start node: 0
Enter goal node: 4
"""