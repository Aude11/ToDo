#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""
import unittest
from unittest import TestCase, mock
from unittest.mock import patch, Mock, MagicMock
import io
from Program import Program
from ToDoRepo import ToDoRepo
from Command import Command
from CommandLineUi import CommandLineUi
from DualLanguageCommandParser import DualLanguageCommandParser
from UserInput import UserInput
from UserInputData import UserInputData
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj


def _CreateCommandLineUi(UserInput=None):
    if (UserInput is None):
        UserInput = _CreateUserInput()
    return CommandLineUi(UserInput)


def _CreateUserInput():
    userinput = Mock()
    data = UserInputData('Add', 'item')
    userinput.handleInput.return_value = data
    return userinput


class TestCommandLineUI(unittest.TestCase):

    def test_when_ui_asked_register_controller_then_it_assigns_controller_its_properties(self):
        controller_mock = Mock()
        ui = _CreateCommandLineUi()
        ui.registerController(controller_mock)
        self.assertEqual(ui.controller, controller_mock)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_empty_todo_when_ui_asked_run_onDisplayDataChanged_then_it_prints_comment(self, mock_stdout):
        todo = {}
        ui = _CreateCommandLineUi()
        ui.onDisplayDataChanged(todo)
        assert mock_stdout.getvalue() == 'Nothing to do! Great! Relax :)\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_todo_when_ui_asked_run_onDisplayDataChanged_then_it_prints_todo(self, mock_stdout):
        todo = {1: "A"}
        ui = _CreateCommandLineUi()
        ui.onDisplayDataChanged(todo)
        assert mock_stdout.getvalue() == ' 1. A\n'

    def test_given_UserInput_handle_returns_obj_when_ui_asked_run_manageInput_then_controller_calls_run(self):
        controller_mock = Mock()
        ui = _CreateCommandLineUi(UserInput=None)
        ui.registerController(controller_mock)
        ui.manageInput()
        controller_mock.run.assert_called_once()

    def test_given_UserInput_handle_returns_None_when_ui_asked_run_manageInput_then_controller_not_called(self):
        controller_mock = Mock()
        mockThatReturnsNone = Mock()
        mockThatReturnsNone.handleInput.return_value = None
        ui = _CreateCommandLineUi(UserInput=mockThatReturnsNone)
        ui.registerController(controller_mock)
        ui.manageInput()
        controller_mock.run.assert_not_called()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_when_ui_asked_run_manageInput_then_notification_message_raised(self, mock_stdout):
        ui = _CreateCommandLineUi()
        ui.manageInput()
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    def test_given_controller_not_registered_when_ui_asked_run_manageInput_then_controller_run_not_called(self):
        controller = Mock()
        ui = _CreateCommandLineUi()
        ui.manageInput()
        controller.run.assert_not_called()

    @patch('CommandLineUi.CommandLineUi.manageInput', return_value=Command.QUIT)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_ui__been_given_user_instruction_to_exit_then_ui_stops_runApplication_loop(self, mock_stdout, mock):
        ui = _CreateCommandLineUi()
        ui.runApplication()
        assert mock_stdout.getvalue() == 'You have exited the application\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_ui_calls_displayIncorrectInput_it_returns_print_message(self, mock_stdout):
        ui = _CreateCommandLineUi()
        ui.displayIncorrectInput()
        assert mock_stdout.getvalue() == 'Invalid input:\nThe input instruction following the command (Add, Delete or Edit)\nis incorrect. Please use the correct syntax:\n Add item\n Delete 1\n Edit 1 newItem\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_ui_calls_displayOperationDBFail_it_returns_print_message(self, mock_stdout):
        ui = _CreateCommandLineUi()
        ui.displayOperationDbFail()
        assert mock_stdout.getvalue() == 'Operation statement executed failed.\n'



if __name__ == '__main__':
    unittest.main()
