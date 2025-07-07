#!/usr/bin/python3
"""Defines a square class with size, position, area, and custom printing."""


class Square:
    """Represents a square with validated size and position, area calculation,
    and a custom printing method.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
                Must be a non-negative integer.
            position (tuple, optional): The position of the square as
                (x, y) coordinates. Defaults to (0, 0).
                Must be a tuple of two non-negative integers.
        """
        self.size = size  # Calls the size setter for validation
        self.position = position  # Calls the position setter for validation

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

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The current position of the square as (x, y) coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.

        Args:
            value (tuple): The new position of the square as (x, y) coordinates.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square to stdout using the character '#',
        offset by its position.

        If the size is 0, prints an empty line.
        Position (x, y) affects print: y adds blank lines before,
        x adds leading spaces to each row of the square.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
