#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:39:45 2021

@author: vernet01
"""
from ToDoRepo import ToDoRepo
from UiNotifierToDoRepo import UiNotifierToDoRepo
from Command import Command
from CommandLineUi import CommandLineUi
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj
from IncorrectInputObj import IncorrectInputObj


class Program():
    def __init__(self, model):
        self.model = model
        self.view = None

    def run(self, actionObj):
        if actionObj.command == Command.ADD:
            self.model.createToDo(actionObj.itemToAdd)
        elif actionObj.command == Command.DELETE:
            self.model.deleteToDo(actionObj.itemNb)
        elif actionObj.command == Command.EDIT:
            self.model.editToDo(actionObj.itemNb, actionObj.newValue)
        elif actionObj.command == Command.USERERROR:
            if self.view is None:
                print("UI has not been registered")
            else:
                self.view.displayIncorrectInput()

    def registerUi(self, ui):
        self.view = ui

    def _notifyDisplayDataChanged(self):
        todo = self.model.readAll()
        if self.view is None:
            print("UI has not been registered")
        else:
            self.view.onDisplayDataChanged(todo)

    def onDataChanged(self):
        self._notifyDisplayDataChanged()

    def onDbOperationFail(self):
        self._notifyOperationDbFail()

    def _notifyOperationDbFail(self):
        if self.view is None:
            print("UI has not been registered")
        else:
            self.view.displayOperationDbFail()
