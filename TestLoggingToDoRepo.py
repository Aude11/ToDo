import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock
import io
from ToDoRepo import ToDoRepo
from LoggingToDoRepo import LoggingToDoRepo


def _CreateLoggingToDoRepo(toDoRepo=None):
    if (toDoRepo is None):
        toDoRepo = MagicMock()
    return LoggingToDoRepo(toDoRepo)

def _ReturnTrue():
    return _ReturnsToDoRepo(True)

def _ReturnFalse():
    return _ReturnsToDoRepo(False)

def _ReturnsToDoRepo(isSuccess):
    toDoRepo = MagicMock()
    toDoRepo.editToDo.return_value = isSuccess
    toDoRepo.createToDo.return_value = isSuccess
    toDoRepo.deleteToDo.return_value = isSuccess
    return toDoRepo


class TestLoggingToDoRepo(unittest.TestCase):

    def test_when_LoggingToDoRepo_call_createToDo_then_it_returns_decorated_createToDo(self):
        toDoRepo = MagicMock()
        toAdd = Mock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        result = loggingToDoRepo.createToDo(toAdd)
        expected = toDoRepo.createToDo(toAdd)
        self.assertEqual(expected, result)

    def test_when_LoggingToDoRepo_calls_deleteToDo_then_it_returns_decorated_deleteToDo(self):
        toDoRepo = MagicMock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        mockToDelete = Mock()
        result = loggingToDoRepo.deleteToDo(mockToDelete)
        expected = toDoRepo.deleteToDo(mockToDelete)
        self.assertEqual(expected, result)

    def test_when_LoggingToDoRepo_calls_readAll_then_it_returns_decorated_readAll(self):
        toDoRepo = MagicMock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        result = loggingToDoRepo.readAll()
        expected = toDoRepo.readAll()
        self.assertEqual(expected, result)

    def test_when_LoggingToDoRepo_calls_editToDo_then_it_returns_decorated_editToDo(self):
        toDoRepo = MagicMock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        mockNbItem = Mock()
        mockToEdit = Mock()
        result = loggingToDoRepo.editToDo(mockNbItem, mockToEdit)
        expected = toDoRepo.editToDo(mockNbItem, mockToEdit)
        self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_LoggingToDoRepo_call_readAll_then_it_raises_message(self,mock_stdout):
        loggingToDoRepo = _CreateLoggingToDoRepo()
        loggingToDoRepo.readAll()
        assert mock_stdout.getvalue() == 'readAll has been called\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_createToDo_returns_True_when_LoggingToDoRepo_call_createToDo_then_it_raises_message_with_result_True(self,mock_stdout):
        toDoRepo = _ReturnTrue()
        toAdd = Mock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        loggingToDoRepo.createToDo(toAdd)
        assert mock_stdout.getvalue() == 'createToDo has been called, result:True\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_deleteToDo_returns_True_when_LoggingToDoRepo_call_deleteToDo_then_it_raises_message_with_result_True(self,mock_stdout):
        toDoRepo = _ReturnTrue()
        toDelete= Mock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        loggingToDoRepo.deleteToDo(toDelete)
        assert mock_stdout.getvalue() == 'deleteToDo has been called, result:True\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_editToDo_returns_True_when_LoggingToDoRepo_call_editToDo_then_it_raises_message_with_result_True(self,mock_stdout):
        toDoRepo = _ReturnTrue()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        mockNbItem = Mock()
        mockToEdit = Mock()
        loggingToDoRepo.editToDo(mockNbItem, mockToEdit)
        assert mock_stdout.getvalue() == 'editToDo has been called, result:True\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_createToDo_returns_False_when_LoggingToDoRepo_call_createToDo_then_it_raises_message_with_result_False(self,mock_stdout):
        toDoRepo = _ReturnFalse()
        toAdd = Mock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        loggingToDoRepo.createToDo(toAdd)
        assert mock_stdout.getvalue() == 'createToDo has been called, result:False\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_deleteToDo_returns_False_when_LoggingToDoRepo_call_deleteToDo_then_it_raises_message_with_result_False(self,mock_stdout):
        toDoRepo = _ReturnFalse()
        toDelete= Mock()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        loggingToDoRepo.deleteToDo(toDelete)
        assert mock_stdout.getvalue() == 'deleteToDo has been called, result:False\n'

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_decorated_editToDo_returns_False_when_LoggingToDoRepo_call_editToDo_then_it_raises_message_with_result_False(self,mock_stdout):
        toDoRepo = _ReturnFalse()
        loggingToDoRepo = _CreateLoggingToDoRepo(toDoRepo)
        mockNbItem = Mock()
        mockToEdit = Mock()
        loggingToDoRepo.editToDo(mockNbItem, mockToEdit)
        assert mock_stdout.getvalue() == 'editToDo has been called, result:False\n'


if __name__ == '__main__':
    unittest.main()