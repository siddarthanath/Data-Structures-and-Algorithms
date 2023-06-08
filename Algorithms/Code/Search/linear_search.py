"""
This file performs Linear Search.
"""
# -------------------------------------------------------------------------------------------------------------------- #
# Standard Library
from typing import List, Union

# Third Party

# Private

# -------------------------------------------------------------------------------------------------------------------- #


# Linear Search Algorithm


class LinearSearch:
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
        """This performs linear search."""
        # Check list compatibility
        self.check_list()
        # Loop through entire list to check if value exists
        print("Initiate Linear Search... \n")
        for i in range(len(self.original_list)):
            print(f"- Iteration {i}...")
            # Check existence
            if self.original_list[i] == self.value:
                # Return the index of the value (NOTE: You can also return True, if you do not care about the position.)
                print(f"The value is in position: {i} \n")
                print("Linear Search complete...")
                # NOTE: The non-optimal search would go to the end of the list and not break early if the value is found!
                return
        # If value does not exist (NOTE: You can also return False.)
        print("Linear Search complete...")
        return -1
