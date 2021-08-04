#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:49:27 2021

@author: vernet01
"""
import unittest
from FrenchCommandParser import FrenchCommandParser
from Command import Command


class TestFrenchCommandParser(unittest.TestCase):

    def test_given_a_string_Ajoute_then_create_a_CommandADD_object(self):
        # Arrange : create a string
        string = "Ajoute"
        french_object = FrenchCommandParser()
        # Act : create an Command Object
        command_object = french_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.ADD)

    def test_given_a_string_Quitte_then_create_a_CommandQUIT_object(self):
        # Arrange : create a string
        string = "Quitte"
        french_object = FrenchCommandParser()
        # Act : create an Command Object
        command_object = french_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.QUIT)

    def test_given_a_string_Efface_then_create_a_CommandDELETE_object(self):
        # Arrange : create a string
        string = "Efface"
        french_object = FrenchCommandParser()
        # Act : create an Command Object
        command_object = french_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.DELETE)

    def test_given_a_string_Modifie_then_create_a_CommandEDIT_object(self):
        # Arrange : create a string
        string = "Modifie"
        french_object = FrenchCommandParser()
        # Act : create an Command Object
        command_object = french_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.EDIT)

    def test_given_a_string_not_incluing_in_statement_then_return_None(self):
        # Arrange : create a string
        string = "random"
        french_object = FrenchCommandParser()
        # Act : create an Command Object
        command_object = french_object.parse(string)
        # Assert
        self.assertEqual(command_object, Command.NONE)


if __name__ == '__main__':
    unittest.main()
