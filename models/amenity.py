#!/usr/bin/python3
"""Create the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Express an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
