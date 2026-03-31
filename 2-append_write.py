#!/usr/bin/python3
"""Module for append_write function."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
