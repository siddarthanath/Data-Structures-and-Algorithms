# ───────────────────────────────────────────────────── Imports ────────────────────────────────────────────────────── #

# Standard Library
# Third Party Library
from pydantic import BaseModel, Field, validator
from loguru import logger
# Private Library

# ────────────────────────────────────────────────────── Code ──────────────────────────────────────────────────────── #
""" 
NOTE:

1. This approach does not contain methods for setting and getting but instead relies on 
instance attribute assignment.
"""

class Flower_4(BaseModel):
    
    """Write a Python class, Flower, that has three instance variables of type str,
    int, and float, that respectively represent the name of the flower, its number of petals, 
    and its price. Your class must include a constructor method that initializes each variable 
    to an appropriate value, and your class should include methods for setting the value of each 
    type, and retrieving the value of each type."""

    name: str = Field(..., min_length=1, description='Name of flower.')
    num_of_petals: int = Field(..., ge=0, description='Number of petals.')
    price: float = Field(..., ge=0, description='Price of flower.')
    
    @validator('name')
    def name_must_be_string(cls, v):
        """This function checks that the name is a string.

        Args:
            v (Any): The attribute to validate.

        Raises:
            ValueError: If name is not string.

        Returns:
            str: Name.
        """
        if not isinstance(v, str):
            raise ValueError("Name must be a string.")
        logger.info('Setting name of flower...')
        return v

    @validator('num_of_petals')
    def petals_must_be_int(cls, v):
        """This function checks that the numbef of petals is an int.

        Args:
            v (Any): The attribute to validate.

        Raises:
            ValueError: If number of petals is not an int.

        Returns:
            int: Number of petals.
        """
        if not isinstance(v, int):
            raise ValueError("Number of petals must be an integer.")
        logger.info('Setting number of petals of flower...')
        return v

    @validator('price')
    def price_must_be_float(cls, v):
        """This function checks that the price is a float.

        Args:
            v (Any): The attribute to validate.

        Raises:
            ValueError: If price is not a float.

        Returns:
            float: Price.
        """
        if not isinstance(v, float):
            raise ValueError("Price must be a float.")
        logger.info('Setting price of flower...')
        return v

    class Config:
        # Validate assignments after creation:
        validate_assignment = True

   

if __name__ == "__main__":
    flower = Flower_4(name='Dandelion',
                      num_of_petals=5,
                      price=20.5)
    print(flower.name)
    print(flower.num_of_petals)
    print(flower.price)
    flower.name = 'Bushy'
    print(flower.name)