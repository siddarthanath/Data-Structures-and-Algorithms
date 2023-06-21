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


def linear_search(input_list: List[Union[float, int]], value: Union[float, int]) -> List[Union[float, int]]:
    # Loop through entire list to check if value exists
    print("Initiate Linear Search... \n")
    for i in range(len(input_list)):
        # Check existence
        if input_list[i] == value:
            # Return the index of the value (NOTE: You can also return True, if you do not care about the position.)
            print(f"The value is in position: {i} \n")
            print("Linear Search complete!")
            # NOTE: The non-optimal search would go to the end of the list and not break early if the value is found!
            return
    # If value does not exist (NOTE: You can also return False.)
    print("Value does not exist in list... \n")
    print("Linear Search complete!")
