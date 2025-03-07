# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
from loguru import logger
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #

class Flower_3:
    
    """Write a Python class, Flower, that has three instance variables of type str,
    int, and float, that respectively represent the name of the flower, its number of petals, 
    and its price. Your class must include a constructor method that initializes each variable 
    to an appropriate value, and your class should include methods for setting the value of each 
    type, and retrieving the value of each type."""

    def __init__(self, name: str, num_of_petals: int, price: float):
        self.name = name
        self.num_of_petals = num_of_petals
        self.price = price
    
    @property
    def name(self) -> str:
        """This function returns the name of the flower.

        Returns:
            str: Name of flower.
        """
        logger.info('Getting name of flower...')
        return self._name
    
    @name.setter
    def name(self, val: str):
        """This function sets the value of the name of the flower.

        Args:
            val (str): The name of flower.

        Raises:
            ValueError: If the flower name is not a string.
        """
        if not isinstance(val, str):
            raise ValueError('Flower name must be a string.')
        logger.info('Setting name of flower...')
        self._name = val
    
    @property
    def num_of_petals(self) -> int:
        """This function returns the number of petals of the flower.

        Returns:
            int: Number of petals of the flower.
        """
        logger.info('Getting number of petals of flower...')
        return self._num_of_petals
    
    @num_of_petals.setter
    def num_of_petals(self, val: int):
        """This function sets the value of the number of petals of the flower.

        Args:
            val (str): The name of flower.

        Raises:
            ValueError: If the flower petal number is not an int.
        """
        if not isinstance(val, int):
            raise ValueError('Flower petal number must be a int.')
        logger.info('Setting number of petals of flower...')
        self._num_of_petals = val
    
    @property
    def price(self) -> float:
        """This function returns the price of the flower.

        Returns:
            float: Price of the flower.
        """
        logger.info('Getting price of flower...')
        return self._price
    
    @price.setter
    def price(self, val: int):
        """This function sets the value of the price of the flower.

        Args:
            val (str): The price of the flower.

        Raises:
            ValueError: If the flower price is not an float.
        """
        if not isinstance(val, float):
            raise ValueError('Flower price must be a float.')
        logger.info('Setting price of flower...')
        self._price = val
   

if __name__ == "__main__":
    flower = Flower_3(name='Dandelion',
                      num_of_petals=5,
                      price=20.5)
    print(flower.name)
    print(flower.num_of_petals)
    print(flower.price)
    flower.name = 'Bushy'
    print(flower.name)