#!/usr/bin/python3
"""
This class is a representation of a place

"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This represent a place

    Attributes:
        city_id (str): contains the City id.
        user_id (str): contians the User id.
        name (str): refers to the name of the place
        description (str): contains the description of the place
        number_rooms (int): contains the numbers of rooms
        number_bathrooms (int): This contains to the number of bathroom
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): the price of a night
        latitude (float): latitude of the place.
        longitude (float): longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
