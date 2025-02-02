import random
from datetime import datetime

from Configs.taskPriority import Priority
from Configs.taskStatus import Status


class Task:
    def __init__(self, taskname : str, des : str, due : datetime, owner=None, assignedTo=None,prio=Priority.LOW):
        self.Id = random.randint(0,10000000)
        self.taskName = taskname
        self.description = des
        self.creationDate = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
        self.duedate = due.strftime("%Y-%m-%d %H-%M-%S")
        self.status = Status.PENDING
        self.priority = prio
        self.owner = owner
        self.assignedTo = assignedTo

    def getId(self):
        return self.Id

    def getName(self):
        return self.taskName

    def getStatus(self):
        return self.status

    def getPriority(self):
        return self.priority

    def getDescription(self):
        return self.description

    def getCreationDate(self):
        return self.creationDate

    def getDueDate(self):
        return self.duedate

    def getOwner(self):
        return self.owner

    def getAssignee(self):
        return self.assignedTo

    def setDueDate(self, d :datetime):
        self.duedate = d

    def setName(self, name):
        self.taskName = name

    def setStatus(self, status):
        self.status = status

    def setPriority(self, prio):
        self.priority = prio

    def setDescription(self, des):
        self.description = des

    def setAssignee(self, user):
        self.assignedTo = user

    def reminder(self):
        self.assignedTo.notifyUser(f"This is a reminder to complete the task")