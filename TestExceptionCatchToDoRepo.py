import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock
import io
from ToDoRepo import ToDoRepo
from ExceptionCatchToDoRepo import ExceptionCatchToDoRepo

def _CreateExceptionCatchToDoRepo(toDoRepo=None):
    if (toDoRepo is None):
        toDoRepo = MagicMock()
    return ExceptionCatchToDoRepo(toDoRepo)

def _ReturnException():
    toDoRepo = MagicMock()
    toDoRepo.createToDo.side_effect = Exception
    toDoRepo.deleteToDo.side_effect = Exception
    toDoRepo.editToDo.side_effect = Exception
    toDoRepo.readAll.side_effect = Exception
    return toDoRepo


class TestExceptionCatchToDoRepo(unittest.TestCase):

    def test_given_decorated_createToDo_raises_an_exception_when_ExceptionCatchToDoRepo_createToDo_called_then_it_returns_False(self):
        toAdd = Mock()
        toDoRepo = _ReturnException()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.createToDo(toAdd)
        expected = False
        self.assertEqual(expected, result)

    def test_given_decorated_deleteToDo_raises_an_exception_when_ExceptionCatchToDoRepo_deleteToDo_called_then_it_returns_False(self):
        toDelete = Mock()
        toDoRepo = _ReturnException()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.deleteToDo(toDelete)
        expected = False
        self.assertEqual(expected, result)

    def test_given_decorated_editToDo_raises_an_exception_when_ExceptionCatchToDoRepo_editToDo_called_then_it_returns_False(self):
        toEdit = Mock()
        NbItem = Mock()
        toDoRepo = _ReturnException()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.editToDo(NbItem, toEdit)
        expected = False
        self.assertEqual(expected, result)

    def test_given_decorated_readAll_raises_an_exception_when_ExceptionCatchToDoRepo_readAll_called_then_it_returns_empty_dict(self):
        toDoRepo = _ReturnException()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.readAll()
        expected = {}
        self.assertEqual(expected, result)

    def test_given_decorated_createToDo_executed_when_ExceptionCatchToDoRepo_createToDo_called_then_it_returns_decorated_createToDo(self):
        toDoRepo = MagicMock()
        toAdd = Mock()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.createToDo(toAdd)
        expected = toDoRepo.createToDo(toAdd)
        self.assertEqual(expected, result)

    def test_given_decorated_deleteToDo_executed_when_ExceptionCatchToDoRepo_deleteToDo_called_then_it_returns_decorated_deleteToDo(self):
        toDoRepo = MagicMock()
        toDelete = Mock()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.deleteToDo(toDelete)
        expected = toDoRepo.deleteToDo(toDelete)
        self.assertEqual(expected, result)

    def test_given_decorated_editToDo_executed_when_ExceptionCatchToDoRepo_editToDo_called_then_it_returns_decorated_editToDo(self):
        toDoRepo = MagicMock()
        toEdit = Mock()
        NbItem = Mock()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.editToDo(NbItem, toEdit)
        expected = toDoRepo.editToDo(NbItem, toEdit)
        self.assertEqual(expected, result)

    def test_given_decorated_readAll_executed_when_ExceptionCatchToDoRepo_readAll_called_then_it_returns_decorated_readAll(self):
        toDoRepo = MagicMock()
        exceptionCatchToDoRepo = _CreateExceptionCatchToDoRepo(toDoRepo)
        result = exceptionCatchToDoRepo.readAll()
        expected = toDoRepo.readAll()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()