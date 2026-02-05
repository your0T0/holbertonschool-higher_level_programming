#!/usr/bin/python3
"""Defines a Student class with reload capability"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation with optional filtering"""
        if isinstance(attrs, list):
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes from dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
