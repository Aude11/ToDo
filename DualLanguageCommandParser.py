#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:38:34 2021

@author: vernet01
"""
from Command import Command
from CommandParser import CommandParser
from FrenchCommandParser import FrenchCommandParser
from EnglishCommandParser import EnglishCommandParser


class DualLanguageCommandParser(CommandParser):
    def __init__(self, parser1, parser2):
        CommandParser.__init__(self)
        self.parser1 = parser1
        self.parser2 = parser2

    def parse(self, toParse):
        result = self.parser1.parse(toParse)
        if (Command.NONE != result):
            return result
        return self.parser2.parse(toParse)
