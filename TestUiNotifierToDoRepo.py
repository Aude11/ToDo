import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock
import io
from DatabaseToDoRepo import DatabaseToDoRepo
from ToDoRepo import ToDoRepo
from UiNotifierToDoRepo import UiNotifierToDoRepo


def _CreateUiNotifierToDoRepo(decorated=None):
    if (decorated is None):
        decorated = MagicMock()
    return UiNotifierToDoRepo(decorated)

def _CreateDecoratedReturnsSuccess(isSuccess):
    decorated = MagicMock()
    decorated.createToDo.return_value = isSuccess
    decorated.editToDo.return_value = isSuccess
    decorated.deleteToDo.return_value = isSuccess
    return decorated

def _CreateDecoratedReturnsTrue():
    return _CreateDecoratedReturnsSuccess(True)

def _CreateDecoratedReturnsFalse():
    return _CreateDecoratedReturnsSuccess(False)


class TestUiNotifierToDoRepo(unittest.TestCase):


    def test_when_UiNotifier_calls_createToDo_then_decorated_createToDo_called(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockItemToAdd = Mock()
        uiNotifier.createToDo(mockItemToAdd )
        decorated.createToDo.assert_called_once()

    def test_when_UiNotifier_calls_deleteToDo_then_decorated_deleteToDo_called(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockItemToDelete = Mock()
        uiNotifier.deleteToDo(mockItemToDelete)
        decorated.deleteToDo.assert_called_once()

    def test_when_UiNotifier_calls_editToDo_then_decorated_editToDo_called(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockNbItem = Mock()
        mockItemToEdit = Mock()
        uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        decorated.editToDo.assert_called_once()

    def test_when_UiNotifier_calls_readAll_then_it_returns_decorated_readAll(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        result = uiNotifier.readAll()
        expected = decorated.readAll()
        self.assertEqual(expected, result)
        decorated.readAll.assert_called()

    def test_when_UiNotifier_calls_createToDo_then_it_returns_decorated_createToDo(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockToAdd = Mock()
        result = uiNotifier.createToDo(mockToAdd)
        expected = decorated.createToDo(mockToAdd)
        self.assertEqual(expected, result)

    def test_when_UiNotifier_calls_deleteToDo_then_it_returns_decorated_deleteToDo(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockToDelete = Mock()
        result = uiNotifier.deleteToDo(mockToDelete)
        expected = decorated.deleteToDo(mockToDelete)
        self.assertEqual(expected, result)

    def test_when_UiNotifier_calls_editToDo_then_it_returns_decorated_editToDo(self):
        decorated = MagicMock()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        uiNotifier.registerController(mockController)
        mockNbItem = Mock()
        mockItemToEdit = Mock()
        result = uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        expected = decorated.editToDo(mockNbItem, mockItemToEdit)
        self.assertEqual(expected, result)

    def test_given_decorated_createToDo_returns_True_when_uiNotifier_createToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToAdd = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.createToDo(mockItemToAdd)
        mockController.onDataChanged.assert_called_once()

    def test_given_decorated_deleteToDo_returns_True_when_uiNotifier_deleteToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToDelete = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.deleteToDo(mockItemToDelete)
        mockController.onDataChanged.assert_called_once()

    def given_decorated_editToDo_returns_True_when_uiNotifier_editToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToEdit = Mock()
        mockNbItem = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        mockController.onDataChanged.assert_called_once()

    def test_given_decorated_createToDo_returns_False_when_uiNotifier_createToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToAdd = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.createToDo(mockItemToAdd)
        mockController.onDbOperationFail.assert_called_once()

    def test_given_decorated_deleteToDo_returns_False_when_uiNotifier_deleteToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToDelete = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.deleteToDo(mockItemToDelete)
        mockController.onDbOperationFail.assert_called_once()

    def given_decorated_editToDo_returns_False_when_uiNotifier_editToDo_called_then_controller_onDataChanged_called(self):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockController = Mock()
        mockItemToEdit = Mock()
        mockNbItem = Mock()
        uiNotifier.registerController(mockController)
        uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        mockController.onDbOperationFail.assert_called_once()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_False_success_when_uiNotifier_createToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToAdd = Mock()
        uiNotifier.createToDo(mockItemToAdd)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_True_success_when_uiNotifier_createToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToAdd = Mock()
        uiNotifier.createToDo(mockItemToAdd)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_False_success_when_uiNotifier_deleteToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToDelete = Mock()
        uiNotifier.deleteToDo(mockItemToDelete)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_True_success_when_uiNotifier_deleteToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToDelete = Mock()
        uiNotifier.createToDo(mockItemToDelete)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_False_success_when_uiNotifier_editToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsFalse()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToEdit = Mock()
        mockNbItem = Mock()
        uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_controller_not_registered_and_True_success_when_uiNotifier_editToDo_called_then_notification_message_raised(self, mock_stdout):
        decorated = _CreateDecoratedReturnsTrue()
        uiNotifier = _CreateUiNotifierToDoRepo(decorated)
        mockItemToEdit = Mock()
        mockNbItem = Mock()
        uiNotifier.editToDo(mockNbItem, mockItemToEdit)
        assert mock_stdout.getvalue() == 'The controller has not been registered\n'
   

if __name__ == '__main__':
    unittest.main()

