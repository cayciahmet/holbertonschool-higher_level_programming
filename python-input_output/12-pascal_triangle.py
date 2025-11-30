#!/usr/bin/python3
"""Pascal's Triangle module."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev = triangle[-1]
        current = [1]
        for i in range(len(prev) - 1):
            current.append(prev[i] + prev[i + 1])
        current.append(1)
        triangle.append(current)
    return triangle
