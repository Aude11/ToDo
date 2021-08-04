#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 23:17:20 2021

@author: vernet01
"""
from Command import Command
from UserInput import UserInput
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj
from IncorrectInputObj import IncorrectInputObj


class CommandLineUi():
    def __init__(self, UserInput):
        self.controller = None
        self.userInput = UserInput

    def manageInput(self):
        if self.controller is None:
            print("The controller has not been registered")
        else:
            actionObj = self.userInput.handleInput()
            if actionObj is not None:
                self.controller.run(actionObj)
                return actionObj.command
        return Command.NONE

    def onDisplayDataChanged(self, todolist):
        if len(todolist) == 0:
            print("Nothing to do! Great! Relax :)")
        else:
            for nb_id, item in todolist.items():
                if item is not None:
                    print(" {0}. {1}".format(nb_id, item))

    def displayIncorrectInput(self):
        print("Invalid input:\nThe input instruction following the command (Add, Delete or Edit)\nis incorrect. Please use the correct syntax:\n Add item\n Delete 1\n Edit 1 newItem")

    def displayOperationDbFail(sef):
        print("Operation statement executed failed.")

    def registerController(self, controller):
        self.controller = controller

    def runApplication(self):
        action = Command.NONE
        while action != Command.QUIT:
            action = self.manageInput()
        print("You have exited the application")
