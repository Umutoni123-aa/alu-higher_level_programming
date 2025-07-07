#!/usr/bin/python3
"""Defines a square class with size validation and property."""


class Square:
    """Represents a square with validated size accessed via property.

    This class provides a square with size encapsulation through properties,
    ensuring size is a non-negative integer and allowing area calculation.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
                Must be a non-negative integer.
        """
        self.size = size # Calls the setter to validate and set __size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
