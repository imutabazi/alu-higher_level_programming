#!/usr/bin/python3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        True if obj is an instance of a_class or a subclass, otherwise False.
    """
    return isinstance(obj, a_class)
