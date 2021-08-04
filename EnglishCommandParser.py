#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:17:36 2021

@author: vernet01
"""
from Command import *
from CommandParser import *


class EnglishCommandParser(CommandParser):
    def __init__(self):
        CommandParser.__init__(self)

    def parse(self, toParse):
        if ("Add" == toParse):
            return Command.ADD
        elif("Exit" == toParse):
            return Command.QUIT
        elif ("Delete" == toParse):
            return Command.DELETE
        elif ("Edit" == toParse):
            return Command.EDIT
        else:
            return Command.NONE
