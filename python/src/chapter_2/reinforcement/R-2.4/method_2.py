# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
from typing import Union
from typing_extensions import Literal
# Third Party Library
from loguru import logger
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

class Flower_2:
    
    """Write a Python class, Flower, that has three instance variables of type str,
    int, and float, that respectively represent the name of the flower, its number of petals, 
    and its price. Your class must include a constructor method that initializes each variable 
    to an appropriate value, and your class should include methods for setting the value of each 
    type, and retrieving the value of each type."""

    def __init__(self, name: str, num_of_petals: int, price: float):
        self.__name = name
        self.__num_of_petals = num_of_petals
        self.__price = price
        # Create store (NOTE: Not the best implementation (why?))
        self.flower_attrs = {'name': self.__name,
                             'num_of_petals': self.__num_of_petals,
                             'price': self.__price}
    
    @staticmethod
    def _check_attr(attr: Literal['name', 'num_of_petals', 'price']):
        """This function checks the validity of the attribute value.

        Args:
            attr (Literal): The attribute of the class. Either 'name', 'num_of_petals' or 'price'.

        Raises:
            ValueError: If attr does not match class attributes.
        """
        if attr not in ['name', 'num_of_petals', 'price']:
            raise ValueError('Variable not present in Flower_1 class!')
        
    def set_value(self, attr: Literal['name', 'num_of_petals', 'price'], val: Union[str, int, float]):
        """This function sets the value of a given attribute.

        Args:
            attr (Literal): The attribute of the class. Either 'name', 'num_of_petals' or 'price'.
            val (Union[str, int, float]): The value of the attribute.
        """
        Flower_2._check_attr(attr=attr)
        logger.info(f'Setting value for {attr} with {val}...')
        self.flower_attrs[attr] = val

    
    def get_value(self, attr: Literal['name', 'num_of_petals', 'price']) -> Union[str, int, float]:
        """This function gets the value of a given attribute.

        Args:
            attr (Literal): The attribute of the class. Either 'name', 'num_of_petals' or 'price'.

        Returns:
            Union[str, int, float]: The attribute value.
        """
        Flower_2._check_attr(attr=attr)
        logger.info(f'Getting value of {attr}...')
        return self.flower_attrs[attr]

if __name__ == "__main__":
    flower = Flower_2(name='Dandelion',
                      num_of_petals=5,
                      price=20.5)
    print(flower.get_value('name'))
    print(flower.get_value('num_of_petals'))
    print(flower.get_value('price'))
    flower.set_value('name', 'Bushy')
    print(flower.get_value('name'))
