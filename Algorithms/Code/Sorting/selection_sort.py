"""
This file performs Selection Sort.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


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
            return self.original_list
        # If length of list is singular, then list is sorted
        if len(self.original_list) == 1:
            return self.original_list
        # If list does not contain all integers or floats, then list cannot be sorted
        if not all(isinstance(x, (int, float)) for x in self.original_list):
            return self.original_list

    def execute(self):
        """This performs selection sort."""
        # Check list compatibility
        self.check_list()
        # Set static pointer
        print("Initiate Selection Sort... \n")
        for i in range(len(self.modify_list)):
            print(f"- Iteration {i}: {self.modify_list} \n")
            # Set current position to be the smallest/largest value (depending on sorting preference)
            temp_val = self.modify_list[i]
            # Set variable pointer
            pointer_2 = i + 1
            # Allow variable counter to reach to the end of the list
            while pointer_2 < len(self.modify_list):
                # Perform selection check
                if eval(f"{temp_val} {self.type_} {self.modify_list[pointer_2]}"):
                    # Update temporary pointer (till optimal swap is found)
                    temp_val, temp_pointer = self.modify_list[pointer_2], pointer_2
                # Increment variable pointer to check through entire list for any potential swaps
                pointer_2 += 1
            # Apply swap (if it has occurred in the iteration)
            if self.modify_list[i] != temp_val:
                self.modify_list[i], self.modify_list[temp_pointer] = (
                    self.modify_list[temp_pointer],
                    self.modify_list[i],
                )
        print("Selection Sort complete...")
