#!/usr/bin/python3
"""
The class represents the city

"""
from models.base_model import BaseModel


class City(BaseModel):
    """ This class describe the City of the users

    Attributes:
        state_id (str): contains the state id.
        name (str): name of the city
    """

    state_id = ""
    name = ""
