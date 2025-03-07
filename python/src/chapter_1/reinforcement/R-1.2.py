# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def is_even(k: int) -> bool:
    """Write a short Python function, is_even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.

    Args:
        k (int): An integer.

    Returns:
        bool: True or False.
    """
    while k > 1:
        k -= 2
    return True if k == 0 else False

if __name__ == "__main__":
    assert is_even(12) == True
    assert is_even(13) != True