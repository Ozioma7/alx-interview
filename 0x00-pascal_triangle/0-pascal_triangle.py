#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Pascal class"""
    if n < 0:
        return []

    triangle = []
    for i in range(n):
        row = []  # First element of each row is always 1
        row.append(1)
        for j in range(1, i):
            # Calculating the elements of the row using the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        if i != 0:
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
