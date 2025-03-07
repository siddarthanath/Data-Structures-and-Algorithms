# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from typing import List, TypeVar, Tuple
# Third Party Library
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #
A = TypeVar('A', int, float)


def minmax(data: List[A]) -> Tuple[A, A]:
    """Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.


    Args:
        data (List[A]): A sequence of numbers.

    Returns:
        Tuple[A, A]: A tuple of length two.
    """
    # NOTE: Would be easier to use in-built sorted function!

    # If sequence only has one value
    if len(data) == 1:
        return (data[0], data[0])
    # Set temporary placement
    (min_temp, max_temp) = (data[0], data[1])
    # Loop through list
    for i in range(2, len(data)):
        # Check if next point is less than the min
        if data[i] < min_temp:
            (min_temp, max_temp) = (data[i], max_temp)
        # Check if next point is more than the max
        elif max_temp < data[i]:
            (min_temp, max_temp) = (min_temp, data[i])
        # If min_temp < data[i] < max_temp, do nothing
    return (min_temp, max_temp)

if __name__ == "__main__":
    assert minmax([2, 4, 3, 6, 7, 8]) == (2, 8)
    assert minmax([1]) == (1, 1)
    assert minmax([2, 2, 2, 2]) == (2, 2)
    assert minmax([9, 25, -1, -6, 55]) == (-6, 55)
    assert minmax([6.9, -2.5, -3.7, 14, 12, 9]) == (-3.7, 14)