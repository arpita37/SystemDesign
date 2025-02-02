from datetime import datetime
from Models.task import Task

class TaskHandler:
    def __init__(self, task : Task):
        self.task = task
        self.msg = f"The task {id} has been updated at {datetime.today().strftime('%H:%M')} time"

    def getTask(self):
        return self.task

    def updateTime(self, d: datetime):
        self.task.setDueDate(d)
        self._Notify()

    def updateName(self, name):
        self.task.setName(name)
        self._Notify()

    def updateStatus(self, status):
        self.task.setStatus(status)
        self._Notify()

    def updatePriority(self, prio):
        self.task.setPriority(prio)
        self._Notify()

    def updateDescription(self, des):
        self.task.setDescription(des)
        self._Notify()

    def updateAssignee(self, user):
        self.task.setAssignee(user)
        self._Notify()

    def _Notify(self):
        if self.task.getAssignee():
            self.task.getAssignee().notifyUser(self.msg, id=self.task.getId())