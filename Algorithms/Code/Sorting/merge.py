"""
This file performs Merge Sort.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


# Merge Sort Algorithm


def merge_sort(input_list: List[Union[float, int]]) -> List[Union[float, int]]:
    # Base case: A list of zero or one elements is sorted, by definition.
    print(input_list)
    if len(input_list) <= 1:
        return input_list
    # Recursive case: First, divide the list into equal-sized sublists consisting of the first half and the second half.
    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]
    print(f"This is the left half (before split): {left_half}")
    print(f"This is the right half (before split): {right_half}")
    # Recursively sort both sublists.
    left_half = merge_sort(left_half)
    print(f"This is left half (after recursion): {left_half}")
    right_half = merge_sort(right_half)
    # Then merge the now-sorted sublists.
    return merge(left_half, right_half)


def merge(
    left_sublist: List[Union[float, int]], right_sublist: List[Union[float, int]]
) -> List[Union[float, int]]:
    # Merge two sorted lists
    result = []
    left_index = 0
    right_index = 0
    # While both lists have elements
    while left_index < len(left_sublist) and right_index < len(right_sublist):
        # If the current element of the left sublist is smaller, add it to the result sublist
        if left_sublist[left_index] < right_sublist[right_index]:
            result.append(left_sublist[left_index])
            left_index += 1
        # If the current element of the right sublist is smaller, add it to the result sublist
        else:
            result.append(right_sublist[right_index])
            right_index += 1
    # Add the remaining elements from the left sublist if any
    while left_index < len(left_sublist):
        result.append(left_sublist[left_index])
        left_index += 1
    # Add the remaining elements from the right sublist if any
    while right_index < len(right_sublist):
        result.append(right_sublist[right_index])
        right_index += 1
    print(f"Result: {result} \n")
    return result
