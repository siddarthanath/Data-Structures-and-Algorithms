# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from typing import List
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

def reverse_list(data: List[int], option: int) -> List[int]:
    """Write a pseudo-code description of a function that reverses a list of n
    integers, so that the numbers are listed in the opposite order than they
    were before, and compare this method to an equivalent Python function
    for doing the same thing.

    Args:
        data (List[int]): A list of integers.
        option (int): The method used.

    Returns:
        List[int]: A list of integers.
    """
    assert 1 <= option <= 3, "Option must be integer between 1 and 3 (inclusive)."
    # Python in-built function
    if option == 1:
        return sorted(data, reverse=True)
    # List slicing
    elif option == 2:
        return data[::-1]
    # Step by step logic
    elif option == 3:
        for i in range(len(data)-1, 0, -1):
            for k in range(len(data)): 
                temp = data[k+1]
                data[k+1] = data[k]
                data[k] = temp
                if k+1 == i:
                    break
        return data

if __name__ == "__main__":
    assert reverse_list([1, 4, 6], 1) == [6, 4, 1]
    assert reverse_list([1, 4, 6], 2) == [6, 4, 1]
    assert reverse_list([1, 4, 6], 3) == [6, 4, 1]