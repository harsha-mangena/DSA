from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    """
    Perform a breadth-first search starting from the given node.

    :param start: The starting node for the search.
    :type start: Any
    :return: None
    """
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Usage
bfs('A')
