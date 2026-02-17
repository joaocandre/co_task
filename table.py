#! /usr/bin/python
"""
Module providing the Table class describing a 2D table/surface.
"""

__author__ = "João André"
__version__ = "1.0"
__maintainer__ = "João André"
__email__ = "jandre@posteo.net"
__date__ = 2026


class Table(object):
    """
    Class describing a table/surface geometry.
    """
    def __init__(self, width, length):
        """
        Constructs a new instance.

        :param      width:   Width of the table
        :type       width:   float
        :param      length:  Length of the table
        :type       length:  float
        """
        super(Table, self).__init__()
        self._width = width
        self._length = length

    @property
    def width(self):
        """
        Get table width.

        :returns:   Table width.
        :rtype:     int
        """
        return self._width

    @property
    def length(self):
        """
        Get table length.

        :returns:   Table length.
        :rtype:     int
        """
        return self._length

    def valid(self, x, y):
        """
        Check if given *x* and *y* coordinates are within table dimensions

        :param      x:    Horizontal position (left to right)
        :type       x:    float
        :param      y:    Vertical position (bottom to top)
        :type       y:    float

        :returns:   True if *(x,y)* within table boundaries, False otherwise.
        :rtype:     bool
        """
        if x < 0 or x > self._width or y < 0 or y > self._length:
            return False

        return True
