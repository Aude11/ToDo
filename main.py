import psycopg2
import sys
from DualLanguageCommandParser import DualLanguageCommandParser
from EnglishCommandParser import EnglishCommandParser
from FrenchCommandParser import FrenchCommandParser
from Program import Program
from CommandLineUi import CommandLineUi
from DatabaseToDoRepo import DatabaseToDoRepo
from UserInput import UserInput
from ActionParser import ActionParser
from ToDoConnectionFactory import ToDoConnectionFactory
from ConnectionFactory import ConnectionFactory
from UiNotifierToDoRepo import UiNotifierToDoRepo
from LoggingToDoRepo import LoggingToDoRepo
from ExceptionCatchToDoRepo import ExceptionCatchToDoRepo
from ForbiddenWordToDb import ForbiddenWordToDb


def main():

    parser = DualLanguageCommandParser(EnglishCommandParser(),
                                       FrenchCommandParser())
    user = "postgres"
    password = "my_password"
    databaseName = "todotest_docker"
    tableName = "todolist_docker"
    port = "5555"
    connectionFactory = ConnectionFactory(user, password, port)
    connection= ToDoConnectionFactory(connectionFactory).createConnectionToDb(databaseName)
    dBmodel = DatabaseToDoRepo(connection, tableName)
    exceptionCatchModel = ExceptionCatchToDoRepo(dBmodel)
    loggingModel = LoggingToDoRepo(exceptionCatchModel)
    forbiddenWordModel = ForbiddenWordToDb(loggingModel)
    model = UiNotifierToDoRepo(forbiddenWordModel)
    actionParser = ActionParser(parser)
    userInput = UserInput(actionParser)
    view = CommandLineUi(userInput)
    controller = Program(model)
    model.registerController(controller)
    view.registerController(controller)
    controller.registerUi(view)
    view.runApplication()
    connection.close()


if __name__ == "__main__":
    main()
