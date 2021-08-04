import psycopg2


class ToDoConnectionFactory():
    def __init__(self, factoryConnection):
        self.factoryConnection = factoryConnection

    def createConnectionToDb(self, databaseName):
        connection = self.factoryConnection.createConnection(None)
        if connection is not None:
            connection.autocommit = True
            isDataBase = self._checkExistenceDb(databaseName, connection)
            connection.close()
            if isDataBase is True:
                return self.factoryConnection.createConnection(databaseName)
            else:
                return None 
        else:
            return None

    def _fetchDataBases(self, connection):
        selectAllDB = "SELECT datname FROM pg_database;"
        cur = connection.cursor()
        cur.execute(selectAllDB)
        databases = cur.fetchall()
        cur.close()
        listDatabase = []
        for database in databases:
            listDatabase.append(database[0])
        return listDatabase

    def _checkExistenceDb(self, databaseName, connection):
        listDataBase = self._fetchDataBases(connection)
        if databaseName in listDataBase:
            return True
        else:
            return False