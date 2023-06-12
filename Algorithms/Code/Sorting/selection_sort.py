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


class SelectionSort:
    def __init__(self, input_list: List[Union[float, int]], type_: str):
        """This initialises general values which will be used repeatedly in the class."""
        self.modify_list = input_list
        self.original_list = input_list.copy()
        self.type_ = None if type_ not in {">", "<"} else type_
        if self.type_ is None:
            raise ValueError(f"Incorrect intialisation for input {type_}!")

    def check_list(self):
        """Check for edge cases for lists."""
        # If values are all the same, then list is sorted
        if len(set(self.original_list)) == 1:
            return True
        # If length of list is singular, then list is sorted
        if len(self.original_list) == 1:
            return True
        # If list does not contain all integers or floats, then list cannot be sorted
        if not all(isinstance(x, (int, float)) for x in self.original_list):
            raise TypeError("Incorrect types in list!")

    def execute(self):
        """This performs selection sort."""
        # Check list compatibility
        if self.check_list():
            print("Returning original list:")
            return self.original_list
        # Set iterable pointer
        print("Initiate Selection Sort... \n")
        for i in range(len(self.modify_list)):
            print(f"- Iteration {i}: {self.modify_list} \n")
            # Set temporary index corresponding to minimum/maximum value
            temp_index = i
            # Loop through from left to right (of the list) to find the index of minimum/maximum value
            for j in range(i+1, len(self.modify_list)):
                # Check if values after the current iterable pointer are greater than/less than the value at minimum/maximum index (and update)
                if eval(f"{self.modify_list[j]} {self.type_} {self.modify_list[temp_index]}"):
                    min_index = j
            # If the index of the minimum/maximum value is not the same as the starting iterable pointer position, 
            if min_index != i:
                self.modify_list[i], self.modify_list[min_index] = self.modify_list[min_index], self.modify_list[i]
        print("Selection Sort complete...")