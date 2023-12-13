def dls(graph, start, goal, depth_limit):
    visited = set()
    stack = [(start, 0)]

    while stack:
        node, depth = stack.pop()
        if depth <= depth_limit:
            if node == goal:
                print(node, end=' ')
                print("\nGoal state reached!")
                return
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                for neighbor in reversed(graph[node]):
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1))
    print("\nGoal state not reached within the depth limit.")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start = 'A'
goal = input("Enter the goal state: ")
depth_limit = int(input("Enter the depth limit: "))
print("DLS starting from node", start, "to goal state", goal, "with depth limit", depth_limit, ":")
dls(graph, start, goal, depth_limit)
