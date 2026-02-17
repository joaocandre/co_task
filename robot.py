#! /usr/bin/python
"""
Module providing the Robot class implementing 2D control of a toy robot.
"""

import math
from enum import Enum
from table import Table


__author__ = "João André"
__version__ = "1.0"
__maintainer__ = "João André"
__email__ = "jandre@posteo.net"
__date__ = 2026


class Robot(object):
    """
    Class describing a 2D robot moving on a table/surface.
    """

    class Heading(Enum):
        """
        Heading enumerator, up/forward-oriented.
        """
        NORTH = 0.0
        SOUTH = math.pi
        EAST = -0.5 * math.pi
        WEST = 0.5 * math.pi

        def __float__(f):
            """
            Convert Heading instance to float (angle, radians)

            :param      f:    Heading to convert.
            :type       f:    Heading

            :returns:   Angle matching *f* heading.
            :rtype:     float
            """
            return f.value

        @staticmethod
        def fromName(name):
            return getattr(Robot.Heading, name)

    def __init__(self, table=None):
        """
        Constructs a new instance.

        :param      table:  Table to place robot on. Defaults to None.
        :type       table:  Table
        """
        super(Robot, self).__init__()
        self._table = table
        self._x = None
        self._y = None
        self._f = None # 0.0
        if self._f in self.Heading:
            self._f = self.Heading(self._f)

    @property
    def table(self):
        return self._table

    def place(self, x, y, f):
        """
        Place(/reset) the robot to target *(x,y)* coordinates with heading *f*.

        :param      x:    Target horizontal position.
        :type       x:    float
        :param      y:    Target vertical position.
        :type       y:    float
        :param      f:    Target heading.
        :type       f:    float

        :returns:   True if on a table and target coordinates are valid, False otherwise.
        :rtype:     bool
        """
        if not self._table:
            return False

        if not self._table.valid(x, y):
            return False

        self._x = x
        self._y = y
        self._f = f

        return True

    def move(self, d=1.0):
        """
        Move the robot forwards for *d* units.

        :param      d:    Forward distance to travel.
        :type       d:    float

        :returns:   True if movement was sucessful, False otherwise.
        :rtype:     bool
        """
        if not self._table or None in (self._x, self._y):
            return False

        _xnext = self._x + round(-1.0 * math.sin(self._f), 9) * d
        _ynext = self._y + round(math.cos(self._f), 9) * d

        if not self._table.valid(_xnext, _ynext):
            return False


        self._x = _xnext
        self._y = _ynext

        return True

    def spin(self, df=0.0):
        """
        Spin the robot *df* radians.

        :param      df:   Angle to spin robot.
        :type       df:   float

        :returns:   True if spin was sucessful, False otherwise.
        :rtype:     bool
        """
        if not self._table:
            return False

        self._f = float(self._f) + df

        if self._f in self.Heading:
            self._f = self.Heading(self._f)

        return True

    def left(self):
        """
        Spin the robot to its left i.e. 90 deg counter-clockwise

        :returns:   True if movement was sucessful, False otherwise.
        :rtype:     bool
        """
        if not self._table:
            return False

        self.spin(0.5 * math.pi)

        return True

    def right(self):
        """
        Spin the robot to its right i.e. 90 deg clockwise

        :returns:   True if movement was sucessful, False otherwise.
        :rtype:     bool
        """
        if not self._table:
            return False

        self.spin(-0.5 * math.pi)

        return True

    def report(self):
        """
        Get robot's current position and heading in the table.

        :returns:   Horizontal position, vertical position and heading of the robot
        :rtype:     tuple of (x, y, f)
        """
        if not self._table:
            return None, None, None

        return self._x, self._y, self._f

