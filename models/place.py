#!/usr/bin/python3
""" This module is a class for Place"""


from models import BaseModel
import models


class Place(BaseModel):
    """ This is the class Place  which inherits from BaseModel"""
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
