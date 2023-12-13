def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node == goal:
            print(node, end=' ')
            print("\nGoal state reached!")
            return

        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    print("\nGoal state not reached.")

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
print("DFS starting from node", start, "to goal state", goal, ":")
dfs(graph, start, goal)
