"""
This file performs Selection Sort.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


# Selection Sort Algorithm


def selection_sort(input_list: List[Union[float, int]]) -> List[Union[float, int]]:
    # Set iterable pointer
    print("Initiate Selection Sort... \n")
    for i in range(len(input_list)):
        print(f"- Iteration {i}: {input_list} \n")
        # Set temporary index corresponding to minimum value
        min_index = i
        # Loop through from left to right (of the list) to find the index of minimum value
        for j in range(i + 1, len(input_list)):
            # Check if values after the current iterable pointer are greater than/less than the value at minimum index (and update)
            if input_list[j] <= input_list[min_index]:
                min_index = j
        # If the index of the minimum value is not the same as the starting iterable pointer position
        if min_index != i:
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    print("Selection Sort complete!")
