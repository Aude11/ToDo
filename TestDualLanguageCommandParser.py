#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:18:07 2021
"""
import unittest
from unittest.mock import Mock
from DualLanguageCommandParser import DualLanguageCommandParser
from parameterized import parameterized
from Command import Command


class TestDualLanguageCommandParser(unittest.TestCase):

    @parameterized.expand([(Command.ADD, Command.NONE),
                           (Command.DELETE, Command.NONE),
                           (Command.EDIT, Command.NONE),
                           (Command.QUIT, Command.NONE)])
    def test_given_parser1_returns_val_and_paser2_returns_NONE_then_dual_returns_val(self, first, second):
        """ Given : pasrse1 returns Command.ADD/Command.LIST/Command.QUIT and
        parser2 returns Command.NONE then DualnagagueCommandParser returns
        the same value as parser1 """
        # Arrange : create  parser1 as a mock that returns first
        # create parser2 as a mock that returns second
        mock_parser1 = Mock()
        mock_parser1.parse.return_value = first
        mock_parser2 = Mock()
        mock_parser2.parse.return_value = second
        # Act : Pass the mocks: DualLanguageCommandParser(parser1, parser2)
        mock_dual = DualLanguageCommandParser(mock_parser1, mock_parser2)
        resuslt = mock_dual.parse('test')
        # Assert
        self.assertEqual(resuslt, first)

    @parameterized.expand([(Command.NONE, Command.ADD),
                           (Command.NONE, Command.DELETE),
                           (Command.NONE, Command.EDIT),
                           (Command.NONE, Command.QUIT)])
    def test_given_parser1_returns_NONE_paser2_returns_val_then_dual_returns_val(self, first, second):
        """ Given : parser1 returns Command.NONE and parser2 returns
        Command.ADD/Command.LIST/Command.QUIT/Command.NONE then dual returns
        the same value as parser2 """
        # Arrange : create  parser1 as a mock that returns first
        # create parser2 as a mock that returns second
        mock_parser1 = Mock()
        mock_parser1.parse.return_value = first
        mock_parser2 = Mock()
        mock_parser2.parse.return_value = second
        # Act : Pass the mocks: DualLanguageCommandParser(parser1, parser2)
        mock_dual = DualLanguageCommandParser(mock_parser1, mock_parser2)
        resuslt = mock_dual.parse('test')
        # Assert
        self.assertEqual(resuslt, second)

    @parameterized.expand([(Command.NONE, Command.NONE)])
    def test_given_parser1_and_paser2_returns_NONE_then_dual_returns_NONE(self, first, second):
        """ Given : parser1 and parser2 returns Command.NONE then dual NONE """
        # Arrange : create  parser1 as a mock that returns first
        # create parser2 as a mock that returns second
        mock_parser1 = Mock()
        mock_parser1.parse.return_value = first
        mock_parser2 = Mock()
        mock_parser2.parse.return_value = second
        # Act : Pass the mocks: DualLanguageCommandParser(parser1, parser2)
        mock_dual = DualLanguageCommandParser(mock_parser1, mock_parser2)
        resuslt = mock_dual.parse('test')
        # Assert
        self.assertEqual(resuslt, Command.NONE)


if __name__ == '__main__':
    unittest.main(verbosity=2)
