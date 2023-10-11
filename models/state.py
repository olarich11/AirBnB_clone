#!/usr/bin/python3
"""Create the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Describe a state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
