#! /usr/bin/python
"""
Script w/ unit tests of the control code of a toy robot as requested by Cellular Origins' inteview coding task,
using the 3 example command sequences provided.
"""

import unittest
from table import Table
from robot import Robot


__author__ = "João André"
__version__ = "1.0"
__maintainer__ = "João André"
__email__ = "jandre@posteo.net"
__date__ = 2026


class ToyRobotTest(unittest.TestCase):
    """
    Class implementing unit testing for the Robot task
    """
    def test_A(self):
        table = Table(5,5)
        robot = Robot(table)

        robot.place(0, 0, Robot.Heading.NORTH)
        robot.move()
        x, y, f = robot.report()
        self.assertEqual(x, 0)
        self.assertEqual(y, 1)
        self.assertEqual(f, Robot.Heading.NORTH)

    def test_B(self):
        table = Table(5,5)
        robot = Robot(table)

        robot.place(0, 0, Robot.Heading.NORTH)
        robot.left()
        x, y, f = robot.report()
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(f, Robot.Heading.WEST)

    def test_C(self):
        table = Table(5,5)
        robot = Robot(table)

        robot.place(1, 2, Robot.Heading.EAST)
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        x, y, f = robot.report()
        self.assertEqual(x, 3)
        self.assertEqual(y, 3)
        self.assertEqual(f, Robot.Heading.NORTH)


if __name__ == '__main__':
    unittest.main()
