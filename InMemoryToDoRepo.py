#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 23:27:38 2021

@author: vernet01
"""
from ToDoRepo import ToDoRepo

class InMemoryToDoRepo(ToDoRepo):
    def __init__(self, todolist):
        self.todolist = todolist

    def readAll(self):
        readtodo = {}
        for nb_id, item in self.todolist.items():
            readtodo.update({nb_id: item})
        return readtodo

    def createToDo(self, toAdd):
        for nb_id, element in self.todolist.items():
            if element is None:
                self.todolist.update({nb_id: toAdd})
                return True
        self.todolist.update({len(self.todolist)+1: toAdd})
        return True

    def editToDo(self, nb_item, toEdit):
        if nb_item in self.todolist.keys():
            self.todolist.update({nb_item: toEdit})
            return True
        return False

    def deleteToDo(self, toDelete):
        if toDelete in self.todolist.keys():
            self.todolist.update({toDelete: None})
            return True
        return False

