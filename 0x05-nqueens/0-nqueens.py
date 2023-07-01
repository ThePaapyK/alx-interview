#!/usr/bin/python3
"""N-Queens Solver"""

import sys

def is_safe(i, j, a, b, c):
    """Check if placing a queen at position (i, j) is safe"""
    return j not in a and i + j not in b and i - j not in c

def queens(n, i=0, a=[], b=[], c=[]):
    """Generator function to find all solutions to the N-Queens problem"""
    if i == n:
        yield a
    else:
        for j in range(n):
            if is_safe(i, j, a, b, c):
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])

def solve(n):
    """Solve the N-Queens problem for a given board size"""
    for solution in queens(n):
        print([[i, s] for i, s in enumerate(solution)])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python nqueens.py N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n)
