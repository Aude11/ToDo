from ToDoRepo import ToDoRepo 


class LoggingToDoRepo(ToDoRepo):
    def __init__(self, toDoRepo):
        self.toDoRepo = toDoRepo

    def createToDo(self, toAdd):
        result = self.toDoRepo.createToDo(toAdd)
        print(f"createToDo has been called, result:{result}")
        return result

    def readAll(self):
        print("readAll has been called")
        return self.toDoRepo.readAll()

    def editToDo(self, nb_item, toEdit):
        result = self.toDoRepo.editToDo(nb_item, toEdit)
        print(f"editToDo has been called, result:{result}")
        return result

    def deleteToDo(self, toDelete):
        result = self.toDoRepo.deleteToDo(toDelete)
        print(f"deleteToDo has been called, result:{result}")
        return result



