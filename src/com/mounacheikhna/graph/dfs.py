# using a stack
def dfs_stack(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex is not visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_recur(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for n in graph[start] - visited:
        dfs_recur(graph, n, visited)
    return visited


g = {'A': {'B', 'C'},
     'B': {'A', 'D', 'E'},
     'C': {'A', 'F'},
     'D': {'B'},
     'E': {'B', 'F'},
     'F': {'C', 'E'}}

print dfs_stack(g, 'A')
print dfs_recur(g, 'A')
