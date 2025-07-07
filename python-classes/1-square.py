#!/usr/bin/python3
"""Defines a square class with a private size attribute."""


class Square:
    """Represents a square with a specific size.

    This class provides a basic representation of a square,
    initializing its size as a private instance attribute.
    """

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
