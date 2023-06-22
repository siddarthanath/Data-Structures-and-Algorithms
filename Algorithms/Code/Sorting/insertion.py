"""
This file performs Insertion Sort.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


# Insertion Sort Algorithm


def insertion_sort(input_list: List[Union[float, int]]) -> List[Union[float, int]]:
    # Set iterable pointer
    print("Initiate Insertion Sort... \n")
    for i in range(1, len(input_list)):
        print(f"- Iteration {i}: {input_list} \n")
        # Apply insert
        insert(input_list[i], input_list, i)
    print(f"- Iteration {i+1}: {input_list} \n")
    print("Selection Sort complete!")


def insert(
    current_val: Union[float, int], input_list: List[Union[float, int]], index: int
):
    # Set iterable pointer
    for j in range(index - 1, -1, -1):
        # Check if current value is larger than indexed value in list
        if current_val >= input_list[j]:
            # Apply insertion
            input_list[j + 1] = current_val
            return
        # Replace value (NOTE: This is similar to selection sort as a "swap".)
        input_list[j + 1] = input_list[j]
    # If all values are being replaced, then the current value belongs at the start
    input_list[0] = current_val
