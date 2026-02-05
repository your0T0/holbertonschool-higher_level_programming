#!/usr/bin/python3
"""Pickling custom class"""

import pickle


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes"""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """Serialize object to file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
