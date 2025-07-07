#!/usr/bin/python3
"""Defines a square class with size validation."""


class Square:
    """Represents a square with size validation.

    This class provides a validated representation of a square,
    ensuring its size is a non-negative integer upon instantiation.
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
