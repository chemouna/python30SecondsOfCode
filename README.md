# python30SecondsOfCode

## Table of Contents

### Math
* [`gcd`](#gcd)
* [`Euler's totient function phi(m)`](#euler-totient-function)
* [`Happy Numbers`](#happy-numbers)
* [`Sierpinski Triangle`](#sierpinski-triangle)

### Graphs
* [`DFS`](#dfs)

[⬆ back to top](#table-of-contents)
## Math
### Pascal Triangle
    1
   1 1
  1 2 1
 1 3 3 1
where each element of each row is either 1 or the sum of the two elements right above it.

```python
def pascal(n):
    """ Prints n rows of pascal's triangle"""
    row = [1]
    k = [0]
    for x in range(max(n, 0)):
        print row
        row = [l + r for l, r in zip(row + k, k + row)]
    return n >> 1
```

[⬆ back to top](#table-of-contents)
## Graphs
### DFS
```python
# using a stack
def dfs_stack(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex is not visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# using recursion
def dfs_recur(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for n in graph[start] - visited:
        dfs_recur(graph, n, visited)
    return visited
```