#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A base class for geometric shapes with area calculation and integer validation.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        This method is not yet implemented and raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a given value is an integer and greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (any): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        # Validate if value is an integer
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        # Validate if value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
