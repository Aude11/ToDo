#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:10:19 2021

@author: vernet01
"""
from Command import Command
from CommandParser import CommandParser


class FrenchCommandParser(CommandParser):
    def __init__(self):
        CommandParser.__init__(self)

    def parse(self, toParse):
        if ("Ajoute" == toParse):
            return Command.ADD
        elif ("Quitte" == toParse):
            return Command.QUIT
        elif ("Efface" == toParse):
            return Command.DELETE
        elif ("Modifie" == toParse):
            return Command.EDIT
        else:
            return Command.NONE
