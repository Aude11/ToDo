from ToDoRepo import ToDoRepo


class UiNotifierToDoRepo(ToDoRepo):
    def __init__(self, decorated):
        self.controller = None
        self.decorated = decorated

    def createToDo(self, toAdd):
        isSuccess = self.decorated.createToDo(toAdd)
        if isSuccess is True:
            self._notifyDataChanged()
        else:
            self._notifyOperationDbFail()
        return isSuccess 

    def readAll(self):
        return self.decorated.readAll()

    def editToDo(self, nb_item, toEdit):
        isSuccess = self.decorated.editToDo(nb_item, toEdit)
        if isSuccess is True:
            self._notifyDataChanged()
        else:
            self._notifyOperationDbFail()
        return isSuccess

    def deleteToDo(self, toDelete):
        isSuccess = self.decorated.deleteToDo(toDelete)
        if isSuccess is True:
            self._notifyDataChanged()
        else:
            self._notifyOperationDbFail()
        return isSuccess

    def registerController(self, controller):
        self.controller = controller
        
    def _notifyDataChanged(self):
        if self.controller is None:
            print("The controller has not been registered")
        else:
            self.controller.onDataChanged()

    def _notifyOperationDbFail(self):
        if self.controller is None:
            print("The controller has not been registered")
        else:
            self.controller.onDbOperationFail()
