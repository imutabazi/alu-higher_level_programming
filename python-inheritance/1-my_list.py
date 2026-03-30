#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A custom list class that inherits from the built-in list."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
