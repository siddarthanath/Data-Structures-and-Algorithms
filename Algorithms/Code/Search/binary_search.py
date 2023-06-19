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


class BinarySearch:
    def __init__(
        self, input_list: List[Union[float, int, str]], value: Union[float, int, str]
    ):
        """This initialises general values which will be used repeatedly in the class."""
        self.original_list = input_list
        self.value = value

    def check_list(self):
        """Check for edge cases for lists."""
        # Check if list is empty
        if len(self.original_list) == 0:
            raise ValueError("List is empty!")

    def execute(self):
        """This performs binary search search."""
        # Check list compatibility
        self.check_list()
        # Set the two pointers (as index)
        start_pointer = 0
        end_pointer = len(self.original_list)-1
        # If value of start pointer is greater than value of end pointer, the value we seek cannot exist (due to ordering)
        while start_pointer <= end_pointer:
            # Set the mid pointer
            mid_pointer = (start_pointer + end_pointer) // 2
            # If the value of the mid pointer is equal to the value we seek
            if self.original_list[mid_pointer] == self.value:
                print(f"The value is in position: {mid_pointer}")
                return 
            # If the value of the mid pointer is greater than the value we seek
            elif self.original_list[mid_pointer] > self.value:
                # Move start pointer
                end_pointer = mid_pointer - 1
            # If the value of the mid pointer is less than the value we seek
            else:
                # Move end pointer
                start_pointer = mid_pointer + 1
        print("Value does not exist in list!")
        return