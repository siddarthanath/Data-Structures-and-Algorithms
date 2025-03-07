# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def sum_of_squares_lt_n(n: int) -> int:
    """Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the positive integers smaller than n.

    Args:
        n (int): An integer.

    Returns:
        int: An integer.
    """
    return (n-1) * (n) * (2*n-1) / 6

if __name__ == "__main__":
    assert sum_of_squares_lt_n(1) == 0
    assert sum_of_squares_lt_n(2) == 1
    assert sum_of_squares_lt_n(3) == 5
    assert sum_of_squares_lt_n(4) == 14
    assert sum_of_squares_lt_n(5) == 30