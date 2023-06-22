"""
This file performs Binary Search.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #

# Binary Search Algorithm


def binary_search(
    input_list: List[Union[float, int]], value: Union[float, int]
) -> List[Union[float, int]]:
    # Set the two pointers (as index)
    start_pointer = 0
    end_pointer = len(input_list) - 1
    # Condition to meet is that the value is found
    print("Initiate Binary Search... \n")
    while start_pointer <= end_pointer:
        # Set the mid pointer
        mid_pointer = (start_pointer + end_pointer) // 2
        # Check if the value of the mid pointer is greater than the value we seek
        if input_list[mid_pointer] == value:
            print(f"The value is in position: {mid_pointer} \n")
            print("Binary Search complete!")
            return
        elif input_list[mid_pointer] > value:
            # Increment
            # Move start pointer
            end_pointer = mid_pointer - 1
        else:
            # Move end pointer
            start_pointer = mid_pointer + 1
    print("Value does not exist in list... \n")
    print("Binary Search complete!")
