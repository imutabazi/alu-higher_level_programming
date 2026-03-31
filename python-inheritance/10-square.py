#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Instantiate a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
