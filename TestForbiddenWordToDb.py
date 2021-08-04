import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock
import io
from parameterized import parameterized
from ToDoRepo import ToDoRepo
from ForbiddenWordToDb import ForbiddenWordToDb


def _CreateForbiddenWordToDb(toDoRepo=None):
    if (toDoRepo is None):
        toDoRepo = MagicMock()
    return ForbiddenWordToDb(toDoRepo)


class TestForbiddenWordToDb(unittest.TestCase):

    @parameterized.expand([("work"),
                           ("homework"),
                           ("paperwork")])
    def test_given_toAdd_belongs_to_forbiddenWord_when_createToDo_called_then_it_returns_False(self, toAdd):
        forbiddenWordToDb = _CreateForbiddenWordToDb()
        result = forbiddenWordToDb.createToDo(toAdd)
        expected = False
        self.assertEqual(expected, result)

    @parameterized.expand([("work"),
                           ("homework"),
                           ("paperwork")])
    def test_given_toEdit_belongs_to_forbiddenWord_when_editToDo_called_then_it_returns_False(self, toEdit):
        forbiddenWordToDb = _CreateForbiddenWordToDb()
        mockNbItem = Mock()
        result = forbiddenWordToDb.editToDo(mockNbItem, toEdit)
        expected = False
        self.assertEqual(expected, result)

    @parameterized.expand([("work"),
                           ("homework"),
                           ("paperwork")])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_toAdd_belongs_to_forbiddenWord_when_createToDo_called_then_it_raises_message(self, toAdd, mock_stdout):
        forbiddenWordToDb = _CreateForbiddenWordToDb()
        forbiddenWordToDb.createToDo(toAdd)
        assert mock_stdout.getvalue() == 'No derogatory language accepted in this to-do\n'

    @parameterized.expand([("work"),
                           ("homework"),
                           ("paperwork")])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_given_toEdit_belongs_to_forbiddenWord_when_editToDo_called_then_it_raises_message(self, toEdit, mock_stdout):
        forbiddenWordToDb = _CreateForbiddenWordToDb()
        mockNbItem = Mock()
        forbiddenWordToDb.editToDo(mockNbItem, toEdit)
        assert mock_stdout.getvalue() == 'No derogatory language accepted in this to-do\n'

    def test_when_ForbiddenWordToDb_calls_deleteToDo_then_it_returns_decorated_deleteToDo(self):
        toDoRepo = MagicMock()
        forbiddenWordToDb = ForbiddenWordToDb(toDoRepo)
        mockToDelete = Mock()
        result = forbiddenWordToDb.deleteToDo(mockToDelete)
        expected = toDoRepo.deleteToDo(mockToDelete)
        self.assertEqual(expected, result)

    def test_when_ForbiddenWordToDb_calls_readAll_then_it_returns_decorated_readAll(self):
        toDoRepo = MagicMock()
        forbiddenWordToDb = ForbiddenWordToDb(toDoRepo)
        result = forbiddenWordToDb.readAll()
        expected = toDoRepo.readAll()
        self.assertEqual(expected, result)

    def test_given_ToAdd_not_in_forbiddenWord_when_ForbiddenWordToDb_calls_createToDo_then_it_return_decorated_createToDo(self):
        toDoRepo = MagicMock()
        forbiddenWordToDb = ForbiddenWordToDb(toDoRepo)
        mockToAdd = Mock()
        result = forbiddenWordToDb.createToDo(mockToAdd)
        expected = toDoRepo.createToDo(mockToAdd)
        self.assertEqual(expected, result)

    def test_given_ToEdit_not_in_forbiddenWord_when_ForbiddenWordToDb_calls_editToDo_then_it_return_decorated_editToDo(self):
        toDoRepo = MagicMock()
        forbiddenWordToDb = ForbiddenWordToDb(toDoRepo)
        mockNbItem = Mock()
        mockToEdit = Mock()
        result = forbiddenWordToDb.editToDo(mockNbItem, mockToEdit)
        expected = toDoRepo.editToDo(mockNbItem, mockToEdit)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
    