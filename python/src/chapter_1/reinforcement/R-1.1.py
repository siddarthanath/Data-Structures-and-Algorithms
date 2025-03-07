# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def is_multiple(n: int, m: int) -> bool:
    """Write a short Python function, is multiple(n, m), that takes two integer
    values and returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.

    Args:
        n (int): An integer.
        m (int): An integer.
    
    Returns:
        bool: True or False.
    """
    # Use modulus
    return True if n % m == 0 else False

if __name__ == "__main__":
    assert is_multiple(9, 3) == True
    assert is_multiple(12, 5) != True