from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            print(vertex, end=' ')
            print("\nGoal state reached!")
            return
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue += graph[vertex]

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

start_vertex = 'A'
goal_vertex = input("Enter the goal state: ")
print("BFS from", start_vertex, "to goal state", goal_vertex, ":")
bfs(graph, start_vertex, goal_vertex)
