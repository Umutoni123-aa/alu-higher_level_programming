#!/usr/bin/python3
"""Defines a square class with size validation and area calculation."""


class Square:
    """Represents a square with size validation and area calculation.

    This class provides a validated representation of a square,
    ensuring its size is a non-negative integer upon instantiation
    and offering a method to compute its area.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the current area of the square.

        Returns:
            int or float: The area of the square (size * size).
        """
        return self.__size * self.__size
