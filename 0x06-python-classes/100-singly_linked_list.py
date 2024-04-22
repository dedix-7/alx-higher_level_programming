#!/usr/bin/python3
""" A module to define a simgly linked lists in python
"""


class Node:
    """ The nodes f the lists
    """

    @property
    def data(self):
        """ A getter for the data attribute of te node
        """

        return (self.__data)

    @data.setter
    def data(self, value):
        """ Setter for teh data of the node
        """

        if (type(value) is not int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value
        return (self.__data)

    @property
    def next_node(self):
        """ next node in the list
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Setter for the next node
        """

        if (type(value) not in [None, Node]):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

    def __init__(self, data, next_node=None):
        """ pseudo constructor for the nide class
        """

        if (type(data) is not int):
            raise TypeError('data must be an integer')
        else:
            self.__data = data
        self.__next_node = next_node


class SinglyLinkedList:
    """ The singly linked lists class
    """

    def __init__(self):
        """struccture for the singly-linked list
        """

        self.head = None

    def sorted_insert(self, value):
        """function to insert and sort values
        """

        new = Node(value, None)
        if (self.head is None):
            self.head = new
            return
        else:
            temp = self.head
            prev = temp
            while (temp is not None):
                if (temp.data < new.data):
                    prev = temp
                    temp = temp.next_node
                else:
                    break
            if (temp is None):
                prev.next_node = new
                return
            if (temp == self.head):
                new.next_node = temp
                self.head = new
                return
            new.next_node = temp
            prev.next_node = new

    def __str__(self):
        """dunder method to print list
        """

        temp = self.head
        out = ""

        while (temp is not None):
            out += str(temp.data) + "\n"
            temp = temp.next_node
        return (out[:-1])
