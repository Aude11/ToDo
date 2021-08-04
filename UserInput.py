#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:39:50 2021

@author: vernet01
"""
from UserInputData import UserInputData
from CommandParser import CommandParser
from ActionParser import ActionParser


class UserInput():
    def __init__(self, ActionParser):
        self.actionParser = ActionParser

    def handleInput(self):
        inputMessage = self.inputuser()
        n = len(inputMessage.split(" ", 2))
        command = inputMessage.split(" ", 1)[0]
        message = None
        if n >= 2:
            message = inputMessage.split(" ", 1)[1]
        userInputData = UserInputData(command, message)
        return self.actionParser.parse(userInputData)

    def inputuser(self):
        return input()
