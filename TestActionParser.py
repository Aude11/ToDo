#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:35:05 2021

@author: vernet01
"""
import unittest
from unittest.mock import Mock
from Command import Command
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj
from CommandObj import CommandObj
from IncorrectInputObj import IncorrectInputObj
from ActionParser import ActionParser


def _CreateAcionParser(commandParser=None):
    if (commandParser is None):
        commandParser = Mock()
    return ActionParser(commandParser)


class TestActionParser(unittest.TestCase):

    def test_given_DataUserInput_with_attribute_add_when_passed_to_parse_then_Action_method_returns_AddObj_object(self):
        mockThatReturnsAdd = Mock()
        mockThatReturnsAdd.parse.return_value = Command.ADD
        action = _CreateAcionParser(commandParser=mockThatReturnsAdd)
        dataUser = Mock()
        dataUser.command = "Add"
        dataUser.message = "Item"
        result = action.parse(dataUser)
        expected = AddObj(Command.ADD, "Item")
        self.assertEqual(expected.command, result.command)
        self.assertEqual(expected.itemToadd, result.itemToadd)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_DELETE_when_passed_to_parse_then_Action_method_returns_DeleteObj_object(self):
        mockThatReturnsDelete = Mock()
        mockThatReturnsDelete.parse.return_value = Command.DELETE
        action = _CreateAcionParser(commandParser=mockThatReturnsDelete)
        dataUser = Mock()
        dataUser.command = "Delete"
        dataUser.message = "1"
        expected = DeleteObj(Command.DELETE, 1)
        result = action.parse(dataUser)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(expected.itemNb, result.itemNb)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_EDIT_when_passed_to_parse_then_action_method_returns_EditObj_object(self):
        mockThatReturnsEdit = Mock()
        mockThatReturnsEdit.parse.return_value = Command.EDIT
        action = _CreateAcionParser(commandParser=mockThatReturnsEdit)
        dataUser = Mock()
        dataUser.command = "Edit"
        dataUser.message = '1 item'
        result = action.parse(dataUser)
        expected = EditObj(Command.EDIT, 1, "item")
        self.assertEqual(expected.command, result.command)
        self.assertEqual(expected.itemNb, result.itemNb)
        self.assertEqual(expected.newValue, result.newValue)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_when_parse_returns_NONE_command_then_action_method_returns_CommandObj_object(self):
        mockThatReturnsNone = Mock()
        mockThatReturnsNone.parse.return_value = Command.NONE
        action = _CreateAcionParser(commandParser=mockThatReturnsNone)
        dataUser = Mock()
        result = action.parse(dataUser)
        expected = CommandObj(Command.NONE)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_when_parse_returns_QUIT_command_then_action_method_returns_CommandObj_object(self):
        mockThatReturnsQuit = Mock()
        mockThatReturnsQuit.parse.return_value = Command.QUIT
        action = _CreateAcionParser(commandParser=mockThatReturnsQuit)
        dataUser = Mock()
        result = action.parse(dataUser)
        expected = CommandObj(Command.QUIT)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_Delete_and_wrong_userinput_when_passed_to_parse_then_returns_IncorrectInput_object(self):
        mockThatReturnsDelete = Mock()
        mockThatReturnsDelete.parse.return_value = Command.DELETE
        action = _CreateAcionParser(commandParser=mockThatReturnsDelete)
        dataUser = Mock()
        dataUser.command = "Delete"
        dataUser.message = 'a'
        result = action.parse(dataUser)
        expected = IncorrectInputObj(Command.USERERROR)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_EDIT_and_wrong_userinput_when_passed_to_parse_then_returns_IncorrectInput_object(self):
        mockThatReturnsEdit = Mock()
        mockThatReturnsEdit.parse.return_value = Command.EDIT
        action = _CreateAcionParser(commandParser=mockThatReturnsEdit)
        dataUser = Mock()
        dataUser.command = "Edit"
        dataUser.message = '1'
        result = action.parse(dataUser)
        expected = IncorrectInputObj(Command.USERERROR)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_EDIT_and_wrong_message_when_passed_to_parse_then_returns_IncorrectInput_object(self):
        mockThatReturnsEdit = Mock()
        mockThatReturnsEdit.parse.return_value = Command.EDIT
        action = _CreateAcionParser(commandParser=mockThatReturnsEdit)
        dataUser = Mock()
        dataUser.command = "Edit"
        dataUser.message = ""
        result = action.parse(dataUser)
        expected = IncorrectInputObj(Command.USERERROR)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_given_DataUserInput_with_attribute_ADD_and_wrong_message_when_passed_to_parse_then_returns_IncorrectInput_object(self):
        mockThatReturnsEdit = Mock()
        mockThatReturnsEdit.parse.return_value = Command.EDIT
        action = _CreateAcionParser(commandParser=mockThatReturnsEdit)
        dataUser = Mock()
        dataUser.command = "Add"
        dataUser.message = ""
        result = action.parse(dataUser)
        expected = IncorrectInputObj(Command.USERERROR)
        self.assertEqual(expected.command, result.command)
        self.assertEqual(type(expected), type(result))

    def test_when_uncorrect_input_given_then_handleInputConcernsNB_returns_None(self):
        parser = _CreateAcionParser()
        wrong_input = "error"
        result = parser.handleInputConcernsNb(wrong_input)
        self.assertEqual(result, None)

    def test_when_correct_digit_input_given_then_handleInputConcernsNB_returns_int(self):
        parser = _CreateAcionParser()
        digit_input = "1"
        result = parser.handleInputConcernsNb(digit_input)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
