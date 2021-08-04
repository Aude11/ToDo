import psycopg2
from ToDoRepo import ToDoRepo


class DatabaseToDoRepo(ToDoRepo):
    def __init__(self, connection, tableName):
        self.connection = connection
        self.tableName = tableName

    def readAll(self):
        todolist = {}
        todoDB = self._getAllDataFromDbTable()
        for item in todoDB:
            todolist.update({item[0]:item[1]})
        return todolist

    def _getAllDataFromDbTable(self):
        read = "SELECT * FROM %s ORDER BY id;" % self.tableName
        cur = self.connection.cursor()
        cur.execute(read)
        todo = cur.fetchall()
        cur.close()
        return todo

    def createToDo(self, toAdd):
        insert = "INSERT INTO %s" % self.tableName + " (item) VALUES (%s);"
        cur = self.connection.cursor()
        cur.execute(insert, (toAdd, ))
        self.connection.commit()
        rowcount = cur.rowcount
        cur.close()
        return rowcount == 1

    def editToDo(self, nb, toUpdate):
        update = "UPDATE %s" % self.tableName + " SET item = %s WHERE id = %s;"
        cur = self.connection.cursor()
        cur.execute(update, (toUpdate, nb))
        self.connection.commit()
        rowcount = cur.rowcount
        cur.close()
        return rowcount == 1

    def deleteToDo(self, toDelete):
        delete = "DELETE FROM %s" % self.tableName + " WHERE id = %s;"
        cur = self.connection.cursor()
        cur.execute(delete, (toDelete,))
        self.connection.commit()
        rowcount = cur.rowcount
        cur.close()
        return rowcount == 1
