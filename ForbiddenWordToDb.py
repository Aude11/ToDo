from ToDoRepo import ToDoRepo 


class ForbiddenWordToDb(ToDoRepo):
    def __init__(self, toDoRepo):
        self.toDoRepo = toDoRepo
        self.forbiddenWord ={"work","homework","paperwork"}

    def createToDo(self, toAdd):
        if toAdd in self.forbiddenWord:
            print("No derogatory language accepted in this to-do")
            return False
        else:
            return self.toDoRepo.createToDo(toAdd)

    def readAll(self):
        return self.toDoRepo.readAll()

    def editToDo(self, nb_item, toEdit):
        if toEdit in self.forbiddenWord:
            print("No derogatory language accepted in this to-do")
            return False
        else:
            return self.toDoRepo.editToDo(nb_item, toEdit)

    def deleteToDo(self, toDelete):
        return self.toDoRepo.deleteToDo(toDelete)
