import heapq

def a_star(graph, heuristic, start, goal):
    pq = []  # (f(n), node)
    heapq.heappush(pq, (heuristic[start], start))

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {start: None}
    visited = set()
    expansions = 0

    while pq:
        f, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        expansions += 1

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_val = new_g + heuristic[neighbor]
                heapq.heappush(pq, (f_val, neighbor))
                parent[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    if node not in parent:
        return None, float('inf'), expansions

    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, g_cost[goal], expansions


# Input
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = {i: [] for i in range(n)}

print("Enter edges (u v cost):")
for _ in range(e):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # remove if directed

# Heuristic input
heuristic = {}
print("Enter heuristic values (node h(n)):")
for _ in range(n):
    node, h = map(int, input().split())
    heuristic[node] = h

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

# Run A*
path, cost, expansions = a_star(graph, heuristic, start, goal)

# Output
if path:
    print("Optimal Path:", path)
    print("Total Cost:", cost)
else:
    print("No path found")

print("Number of node expansions:", expansions)


"""
Enter number of nodes: 5
Enter number of edges: 6
Enter edges (u v cost):
0 1 1
0 2 4
1 3 2
2 3 1
3 4 3
1 4 7

Enter heuristic values (node h(n)):
0 7
1 6
2 2
3 1
4 0

Enter start node: 0
Enter goal node: 4
"""