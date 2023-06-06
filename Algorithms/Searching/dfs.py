graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs_recursive(node):
    """
    Perform a depth-first search on a graph using a recursive approach.

    Args:
    - node: The node to start the search from.

    Returns:
    - None.
    """
    visited.add(node)
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(neighbor)

dfs_recursive('A')

def dfs_iterative(start):
    """
    Performs a depth-first search iteratively starting from a given node.

    Args:
        start: The node to start the search from.

    Returns:
        None.
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
# Usage
dfs_recursive('A')
