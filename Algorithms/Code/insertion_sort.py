"""
This file performs Insertion Sort.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


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
        # Set static pointer
        print("Initiate Insertion Sort... \n")
        for i in range(1, len(self.modify_list)):
            print(f"- Iteration {i-1}: {self.modify_list} \n")
            # Set variable pointer
            pointer = i - 1
            # Check up until the first index
            while pointer >= 0:
                # Perform insertion check
                if eval(
                    f"{self.modify_list[pointer]} {self.type_} {self.modify_list[i]}"
                ):
                    # Apply swap
                    self.modify_list[i], self.modify_list[pointer] = (
                        self.modify_list[pointer],
                        self.modify_list[i],
                    )
                    # NOTE: This boolean is not needed but helps reduce number of swap checks!
                    swap = True
                else:
                    # NOTE: This boolean is not needed but helps reduce number of swap checks!
                    swap = False
                # Decrement static and variable pointer to check through entire list for any potential swaps
                pointer -= 1
                i -= 1
                # If we no longer swap after the first swap instance, we have found the correct position!
                if swap is False:
                    break
        print(f"- Iteration {len(self.modify_list)-1}: {self.modify_list} \n")
        print("Insertion Sort complete...")
