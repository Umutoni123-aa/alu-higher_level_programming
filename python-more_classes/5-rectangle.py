#!/usr/bin/python3
""" Defines the rectangle """


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes the variables"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Rwturns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """assigning the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        r_area = self.__width * self.__height
        return r_area

    def perimeter(self):
        """This will return the perimeter of the rectangle"""
        r_perimeter = 2 * (self.__width + self.__height)

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return r_perimeter

    def __del__(self):
        """Detects the deletion and returns bye when deleted"""
        print("Bye rectangle...")

    def __str__(self):
        """Prints the rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rect = ''
            for i in range(self.__height):
                for x in range(self.__width):
                    rect = rect + '#'

                rect += '\n'
            return rect[:-1]

    def __repr__(self):
        """Prints the string representation officially"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
