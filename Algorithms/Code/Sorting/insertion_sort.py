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


class InsertionSort:
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
        """This performs insertion sort."""
        # Check list compatibility
        if self.check_list():
            print("Returning original list:")
            return self.original_list
        # Set iterable pointer
        print("Initiate Insertion Sort... \n")
        for i in range(1, len(self.modify_list)):
            print(f"- Iteration {i-1}: {self.modify_list} \n")
            # Set variable pointer to current index
            j = i
            # Apply swap only if pointer is not out of range and previous value is greater/less than current value
            while j > 0 and eval(f"{self.modify_list[j-1]} {self.type_} {self.modify_list[j]}"):
                # Apply swap
                self.modify_list[j], self.modify_list[j-1] = self.modify_list[j-1], self.modify_list[j]
                # Decrement variable pointer
                j -= 1
        print(f"- Iteration {len(self.modify_list)-1}: {self.modify_list} \n")
        print("Insertion Sort complete...")