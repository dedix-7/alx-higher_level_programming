#!/usr/bin/python3
""" A script to have a function that gives the name
"""

def say_my_name(first_name, last_name=""):
    """ a function that says a person's name. both first and last

    Args:
         first_name - first name of the person
         last_name = person's last name. it dedaukts to an empty string
    Return:
          None
    Raises:
          TypeError in case any argument is not a string
    """

    if (type(first_name) is not str):
        raise TypeError('first_name must be a string')
    if (type(last_name) is not str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
