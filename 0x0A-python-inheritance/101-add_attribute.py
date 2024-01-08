#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible"""

def add_attribute(obj, attr_name, attr_value):
    """check if a new attribute can be added"""
    if not hasattr(obj, '__dict__') and not hasattr(type(obj), '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
    """set the attribute"""
