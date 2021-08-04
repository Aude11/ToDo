#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 12:05:07 2021

@author: vernet01
"""
import unittest
from unittest.mock import patch, Mock
import io
from Program import Program
from Command import Command
from AddObj import AddObj
from DeleteObj import DeleteObj
from EditObj import EditObj
from IncorrectInputObj import IncorrectInputObj


def _CreateController(model=None):
    if (model is None):
        model = Mock()
    return Program(model)


class TestController(unittest.TestCase):

    def test_when_controller_asked_run_ADD_then_it_calls_model_createToDodo(self):
        controller = _CreateController()
        obj = AddObj(Command.ADD, "item")
        controller.run(obj)
        controller.model.createToDo.assert_called_once()

    def test_when_controller_asked_run_DELETE_then_it_calls_model_deleteToDo(self):
        controller = _CreateController()
        obj = Mock()
        obj.command = Command.DELETE
        controller.run(obj)
        controller.model.deleteToDo.assert_called_once()

    def test_when_controller_asked_run_EDIT_then_it_calls_model_editToDo(self):
        controller = _CreateController()
        obj = Mock()
        obj.command = Command.EDIT
        controller.run(obj)
        controller.model.editToDo.assert_called_once()

    def test_when_controller_asked_run_USERERROR_then_it_calls_model_displayIncorrectInput(self):
        controller = _CreateController()
        obj = Mock()
        obj.command = Command.USERERROR
        view_mock = Mock()
        controller.registerUi(view_mock)
        controller.run(obj)
        controller.view.displayIncorrectInput.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_UI_not_registered_when_controller_asked_run_USERERROR_then_notification_message_raised(self, mock_stdout):
        controller = _CreateController()
        obj = Mock()
        obj.command = Command.USERERROR
        controller.run(obj)
        assert mock_stdout.getvalue() == "UI has not been registered\n"

    def test_when_controller_asked_register_view_then_it_assigns_view_its_properties(self):
        view_mock = Mock()
        controller = _CreateController()
        controller.registerUi(view_mock)
        self.assertEqual(controller.view, view_mock)

    def test_when_controller_is_notified_DataChanged_then_it_raises_displayDataChanged_event_on_UI(self):
        view_mock = Mock()
        controller = _CreateController()
        controller.registerUi(view_mock)
        controller.onDataChanged()
        view_mock.onDisplayDataChanged.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_UI_not_registered_when_controller_is_notified_DataChanged_then_notification_message_raised(self, mock_stdout):
        controller = _CreateController()
        controller.onDataChanged()
        assert mock_stdout.getvalue() == "UI has not been registered\n"

    def test_given_UI_not_registered_when_controller_is_notified_DataChanged_then_view_displayDataChanged_not_called(self):
        controller = _CreateController()
        view = Mock()
        controller.onDataChanged()
        view.onDisplayDataChanged.assert_not_called()

    def test_given_controller_is_notified_DataChanged_then_it_raises_readAll_event_on_model(self):
        view_mock = Mock()
        controller = _CreateController()
        controller.registerUi(view_mock)
        controller.onDataChanged()
        controller.model.readAll.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_UI_not_registered_when_controller_calls_notifyOperationDBFail_then_notification_message_raised(self, mock_stdout):
        controller = _CreateController()
        controller.onDbOperationFail()
        assert mock_stdout.getvalue() == "UI has not been registered\n"

    def test_when_controller_is_notified_OperationDBFail_then_it_raises_displayOperationDBFail_on_UI(self):
        view_mock = Mock()
        controller = _CreateController()
        controller.registerUi(view_mock)
        controller.onDbOperationFail()
        view_mock.displayOperationDbFail.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
