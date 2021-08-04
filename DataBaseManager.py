import psycopg2
from ConnectionFactory import ConnectionFactory
from ToDoConnectionFactory import ToDoConnectionFactory


class DataBaseManager():
    def __init__(self, connectionFactory):
        self.connectionFactory = connectionFactory
        self.toDoConnectionFactory = ToDoConnectionFactory(self.connectionFactory)

    def createDataBase(self, databaseName, tableName):
        connection = self.toDoConnectionFactory.createConnectionToDb(databaseName)
        if connection is None:
            connection = self.connectionFactory.createConnection(None)
            self._ensureDatabaseExists(connection, databaseName)
 
        self._ensureToDoTableExists(connection, tableName)
        connection.close()

    def _ensureDatabaseExists(self, connection, databaseName):
        cur = connection.cursor()
        create_db = "CREATE DATABASE %s;" % databaseName
        cur = connection.cursor()
        cur.execute(create_db)
        cur.close()

    def _ensureToDoTableExists(self, connection, tableName):
        cur = connection.cursor()
        tableCreation = "CREATE TABLE IF NOT EXISTS %s (id SERIAL PRIMARY KEY, item  VARCHAR(50);" % tableName
        cur.execute(tableCreation)
        connection.commit()
        cur.close()
