from ToDoRepo import ToDoRepo

class ExceptionCatchToDoRepo(ToDoRepo):
    def __init__(self, toDoRepo):
        self.toDoRepo = toDoRepo

    def createToDo(self, toAdd):
        try:
            return self.toDoRepo.createToDo(toAdd)
        except:
            return False

    def readAll(self):
        try:
            return self.toDoRepo.readAll()
        except:
            return {}
        
    def editToDo(self, nb_item, toEdit):
        try:
            return self.toDoRepo.editToDo(nb_item, toEdit)
        except:
            return False

    def deleteToDo(self, toDelete):
        try:
            return self.toDoRepo.deleteToDo(toDelete)
        except:
            return False


