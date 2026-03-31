#!/usr/bin/python3
"""Module for pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        prev = tri[-1]
        tmp = [1]
        for i in range(len(prev) - 1):
            tmp.append(prev[i] + prev[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
