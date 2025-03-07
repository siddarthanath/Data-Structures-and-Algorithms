# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from typing import List
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def odd_product(data: List[int], option: int) -> bool:
    """Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.

    Args:
        data (List[int]): A list of integers.
        option (int): The method used.

    Returns:
        bool: True or False.
    """
    assert 1 <= option <= 2, "Option must be integer between 1 and 2 (inclusive)."
    if option == 1:
        pairs = []
        for i in data:
            if i % 2 == 1 and i not in pairs:
                pairs.append(i)
                if len(pairs) == 2:
                    return True


if __name__ == "__main__":
    assert odd_product([2, 3, 4, 5], 1) == True
