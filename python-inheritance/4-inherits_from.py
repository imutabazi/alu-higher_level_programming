#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns:
        True if obj is a subclass of a_class but not exactly a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
