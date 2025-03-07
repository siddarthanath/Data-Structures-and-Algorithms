# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def alternative_r_1_4(n: int) -> int:
    """Give a single command that computes the sum from Exercise R-1.4, 
    relying on Python’s comprehension syntax and the built-in sum function.

    Args:
        n (int): An integer.

    Returns:
        int: An integer.
    """
    return sum([i**2 for i in range(n)])

if __name__ == "__main__":
    assert alternative_r_1_4(1) == 0
    assert alternative_r_1_4(2) == 1
    assert alternative_r_1_4(3) == 5
    assert alternative_r_1_4(4) == 14
    assert alternative_r_1_4(5) == 30
