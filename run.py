#! /usr/bin/python
"""
Script for control of a toy robot as requested by Cellular Origins' inteview coding task,
using either user input or a command sequence from a text file

Interactive usage: <python> run.py
File Usage:        <python> run.py [assets/input.txt]
"""

import sys
from table import Table
from robot import Robot


__author__ = "João André"
__version__ = "1.0"
__maintainer__ = "João André"
__email__ = "jandre@posteo.net"
__date__ = 2026


def parseArguments(args):
    """
    Convert argument list *args* from comma-separated string to list of floats/headings

    :param      args:  Arguments to parse.
    :type       args:  str

    :returns:   List of numerical arguments.
    :rtype:     list
    """
    out = []
    for arg in args.split(','):
        try:
            out.append(float(arg))
        except ValueError:
            out.append(Robot.Heading.fromName(arg))

    return out

def parseCommand(cmd, robot):
    """
    Interpret text command *cmd* as robot movement and arguments and execute on *robot*.

    :param      cmd:    Command to execute.
    :type       cmd:    str
    :param      robot:  Robot to control.
    :type       robot:  Robot
    """
    success = False
    try:
        args = cmd.split(' ')
        do = getattr(robot, args[0].lower())
        if len(args) > 1:
            success = do(*parseArguments(args[1]))
        else:
            success = do()
        if success:
            print(f'{cmd} -> {robot.report()}')
    except (ValueError, AttributeError, IndexError, TypeError):
        print(f'{cmd} -> ERROR: invalid/malformed command.')

    return success


if __name__ == '__main__':
    # initialize table and robot
    table = Table(5,5)
    robot = Robot(table)

    # switch between interactive or input modes according to given cli arguments
    cmd = None
    if len(sys.argv) < 2:
        while True:
            cmd = input('Command: ')
            if cmd in ['EXIT', 'exit']:
                break
            parseCommand(cmd, robot)
    else:
        with open(sys.argv[1], 'r') as file:
            cmds = file.read().split('\n')
            for cmd in cmds:
                if cmd[0] != '#':
                    parseCommand(cmd, robot)
