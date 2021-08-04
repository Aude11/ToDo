#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:34:33 2021

@author: vernet01
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
import io
from Program import Program
from Command import Command
from InMemoryToDoRepo import InMemoryToDoRepo
from Command import Command
from CommandLineUi import CommandLineUi


def _CreateInMemoryToDoRepo(todolist=None):
    if (todolist is None):
        todolist = MagicMock()
    return InMemoryToDoRepo(todolist)


class TestToDoRepo(unittest.TestCase):

    def test_when_model_asked_run_readAll_then_it_returns_current_todo(self):
        todolist = {1: "A", 2: "B"}
        model = _CreateInMemoryToDoRepo(todolist)
        readtodo = model.readAll()
        self.assertEqual(todolist, readtodo)

    def test_given_full_todo_when_model_asked_run_createToDo_then_item_adds_to_todo(self):
        todolist = {1: "A", 2: "B"}
        model = _CreateInMemoryToDoRepo(todolist)
        model.createToDo("C")
        self.assertEqual(todolist, {1: "A", 2: "B", 3: "C"})

    def test_given_todo_when_model_asked_run_editToDo_then_model_modifies_todo(self):
        todolist = {1: "A", 2: "B"}
        model = _CreateInMemoryToDoRepo(todolist)
        model.editToDo(1, "C")
        self.assertEqual(todolist, {1: "C", 2: "B"})

    def test_given_wrong_edit_nb_when_model_asked_run_editToDo_then_todo_not_modified(self):
        todolist = {1: "A", 2: "B"}
        model = _CreateInMemoryToDoRepo(todolist)
        model.editToDo(3, "C")
        self.assertEqual(todolist, {1: "A", 2: "B"})

    def test_given_todo_with_empty_spot_when_model_asked_run_createToDo_then_item_adds_to_empty_spot(self):
        todolist = {1: "A", 2: None}
        model = _CreateInMemoryToDoRepo(todolist)
        model.createToDo("B")
        self.assertEqual({1: "A", 2: "B"}, todolist)

    def test_given_todo_when_model_asked_run_deleteToDo_then_item_deleted(self):
        todolist = {1: "A", 2: "B"}
        model = _CreateInMemoryToDoRepo(todolist)
        model.deleteToDo(2)
        self.assertEqual(todolist, {1: "A", 2: None})


if __name__ == '__main__':
    unittest.main()
