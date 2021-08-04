#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from EnglishCommandParser import EnglishCommandParser
from Command import Command


class TestEnglishCommandParser(unittest.TestCase):

    def test_given_a_string_Add_then_create_a_CommandADD_object(self):
        # Arrange : create a string
        string = "Add"
        english_object = EnglishCommandParser()
        # Act : create an Command Object
        command_object = english_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.ADD)

    def test_given_a_string_Exit_then_create_a_CommandQUIT_object(self):
        # Arrange : create a string
        string = "Exit"
        english_object = EnglishCommandParser()
        # Act : create an Command Object
        command_object = english_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.QUIT)

    def test_given_a_string_Delete_then_create_a_CommandDELETE_object(self):
        # Arrange : create a string
        string = "Delete"
        english_object = EnglishCommandParser()
        # Act : create an Command Object
        command_object = english_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.DELETE)

    def test_given_a_string_Edit_then_create_a_CommandEDIT_object(self):
        # Arrange : create a string
        string = "Edit"
        english_object = EnglishCommandParser()
        # Act : create an Command Object
        command_object = english_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.EDIT)

    def test_given_a_string_not_incluing_in_statement_then_return_None(self):
        # Arrange : create a string
        string = "random"
        english_object = EnglishCommandParser()
        # Act : create an Command Object
        command_object = english_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.NONE)


if __name__ == '__main__':
    unittest.main()
