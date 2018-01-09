# python30SecondsOfCode

## Table of Contents

### Math
* [`Gcd`](#gcd)
* [`Extended Gcd`](#extendedgcd)
* [`Pascal Triangle`](#pascaltriangle)

### Graphs
* [`DFS`](#dfs)

[⬆ back to top](#table-of-contents)
## Math
### Gcd
```python
def gcd(a, b):
    if abs(a) < abs(b):
        gcd(b, a)

    while b > 0:
        q, r = divmod(a, b)
        a, b = b, r

    return a
```

### Extended Gcd
```python
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n

    gcd = b
    return gcd, x, y
```
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