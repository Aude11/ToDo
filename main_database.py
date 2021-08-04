import psycopg2
import sys
from DataBaseManager import DataBaseManager
from ConnectionFactory import ConnectionFactory


def main():

    user = "postgres"
    password = "my_password"
    port = "5555"
    databaseName = "todotest_docker"
    tableName = "todolist_docker"
    connectionFactory = ConnectionFactory(user, password, port)
    databaseManager = DataBaseManager(connectionFactory)
    databaseManager.createDataBase(databaseName, tableName)


if __name__ == "__main__":
    main()
