#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:08:46 2021

@author: vernet01
"""
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock, MagicMock
from UserInput import UserInput
from ActionParser import ActionParser
from Command import Command
from AddObj import AddObj


def _CreateUserInput(ActionParser=None):
    if (ActionParser is None):
        ActionParser = Mock()
    return UserInput(ActionParser)


class TestUserInput(unittest.TestCase):

    @patch('UserInput.UserInput.inputuser', return_value='item1 item2')
    def test_given_string_with_2_parts_when_input_returns_string_then_hanldeInput_returns_DataUserInput_command_attribute_equals_first_segment(self, mock_object):
        user = _CreateUserInput()
        result = user.inputuser()
        self.assertEqual(result, 'item1 item2')

    @patch('UserInput.UserInput.inputuser', return_value='item1 item2')
    def test_given_string_with_2_parts_when_inputuser_returns_string_then_n_equals_2(self, mock_object):
        user = _CreateUserInput()
        inputMessage = user.inputuser()
        n = len(inputMessage.split(" ", 2))
        self.assertEqual(n, 2)

    @patch('UserInput.UserInput.inputuser', return_value='item1')
    def test_given_string_with_1_word_when_input_returns_string_then_n_equals_1(self, mock_object):
        user = _CreateUserInput()
        inputMessage = user.inputuser()
        n = len(inputMessage.split(" ", 2))
        self.assertEqual(n, 1)

    @patch('UserInput.UserInput.inputuser', return_value='item')
    def test_given_string_1_segement_when_input_returns_string_then_hanldeInput_returns_DataUserInput_message_attribute_equals_empty_string(self, mock_object):
        user = _CreateUserInput()
        inputMessage = user.inputuser()
        command = inputMessage.split(" ", 1)[0]
        self.assertEqual(command, 'item')

    @patch('UserInput.UserInput.inputuser', return_value='Add item')
    def test_given_string_with_2_parts_when_handleInput_called__then_returns_(self, mock_object):
        mockThatReturnsAdd = Mock()
        mockThatReturnsAdd.parse.return_value = AddObj(Command.ADD, 'item')
        user = _CreateUserInput(ActionParser=mockThatReturnsAdd)
        result = user.handleInput()
        excepted = AddObj(Command.ADD, 'item')
        self.assertEqual(result.command, excepted.command)
        self.assertEqual(result.itemToadd, excepted.itemToadd)
        self.assertEqual(type(result), type(excepted))


if __name__ == '__main__':
    unittest.main()
