#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock
import io
from DatabaseToDoRepo import DatabaseToDoRepo


def _CreateDatabaseToDoRepo(connection=None, tableName=None):
    if (connection is None):
        connection = MagicMock()
    if (tableName is None):
        tableName = MagicMock()
    return DatabaseToDoRepo(connection, tableName)

def _CreateConnection(data):
    connection = MagicMock()
    mock_cur = connection.cursor()
    mock_cur.fetchall.return_value = data
    return connection

def _ReturnRowCountDbOne():
    connection = MagicMock()
    mock_cur = connection.cursor()
    mock_cur.rowcount = 1
    return connection

def _ReturnRowCountDbZero():
    connection = MagicMock()
    mock_cur = connection.cursor()
    mock_cur.rowcount = 0
    return connection


class TestToDoRepoDB(unittest.TestCase):

    def test_given_data_in_database_when_model_asked_run_readAll_then_it_returns_dict_todo(self):
        data = [(1, 'a'), (2, 'b')]
        connection = _CreateConnection(data)
        model = _CreateDatabaseToDoRepo(connection)
        result = model.readAll()
        expected = {1: "a", 2: "b"}
        self.assertEqual(expected, result)

    def test_given_data_in_database_when_getAllDataFromDbTable_calls_then_it_returns_database_data(self):
        data = [(1, 'a'), (2, 'b')]
        connection = _CreateConnection(data)
        model = _CreateDatabaseToDoRepo(connection)
        expected = [(1, 'a'), (2, 'b')]
        result = model._getAllDataFromDbTable()
        self.assertEqual(expected, result)

    def test_given_inserring_to_database_affects_one_row_when_createToDo_calls_it_returns_True(self):
        connection = _ReturnRowCountDbOne()
        model = _CreateDatabaseToDoRepo(connection)
        mockItemToAdd = Mock()
        result = model.createToDo(mockItemToAdd)
        self.assertTrue(result)
       
    def test_given_inserring_to_database_affects_zero_row_when_createToDo_calls_it_returns_False(self):
        connection = _ReturnRowCountDbZero()
        model = _CreateDatabaseToDoRepo(connection)
        mockAddItem  = Mock()
        result = model.createToDo(mockAddItem)
        self.assertFalse(result)

    def test_given_deleting_to_database_affects_one_row_when_deleteToDo_calls_it_returns_True(self):
        connection = _ReturnRowCountDbOne()
        model = _CreateDatabaseToDoRepo(connection)
        mockItemToDelete  = Mock()
        result = model.createToDo(mockItemToDelete)
        self.assertTrue(result)
       
    def test_given_deleting_to_database_affects_zero_row_when_deleteToDo_calls_it_returns_False(self):
        connection = _ReturnRowCountDbZero()
        model = _CreateDatabaseToDoRepo(connection)
        mockItemToDelete= Mock()
        result = model.createToDo(mockItemToDelete)
        self.assertFalse(result)

    def test_given_updating_to_database_affects_one_row_when_editToDo_calls_it_returns_True(self):
        connection = _ReturnRowCountDbOne()
        model = _CreateDatabaseToDoRepo(connection)
        mockItemToEdit  = Mock()
        mockItemNb = Mock()
        result = model.editToDo(mockItemNb, mockItemToEdit)
        self.assertTrue(result)
       
    def test_given_updating_to_database_affects_zero_row_when_editToDo_calls_it_returns_False(self):
        connection = _ReturnRowCountDbZero()
        model = _CreateDatabaseToDoRepo(connection)
        mockItemToEdit  = Mock()
        mockItemNb = Mock()
        result = model.editToDo(mockItemNb, mockItemToEdit)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
