from datetime import datetime
from threading import Lock
import logging

from Configs.taskStatus import Status
from Handlers.taskHandler import TaskHandler
from Models.task import Task

logging.basicConfig(level=logging.INFO)
from Models.user import User


class TaskManagement:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls.taskList = dict()
            cls.users = dict()
            cls.log = logging.getLogger("TaskManagementSystem")
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls._instance

    def addUser(self, user : User):
        if user.getId() not in self.users:
            self.users[user.getId()] = user
            self.log.info(f"User {user.getName()} has been created successfully")
            return
        self.log.warning(f"User {user.getName()} already exists")

    def deleteUser(self):
        # Have to update tasks for which this user is owner
        # and for those assignedTo this user
        pass

    def addTask(self, task):
        self.taskList[task.getId()] = TaskHandler(task)

    def updateTime(self, task : Task, d: datetime):
        self.taskList[task.getId()].updateTime(d)

    def updateName(self, task, name):
        self.taskList[task.getId()].updateName(name)

    def updateStatus(self, task, status):
        self.taskList[task.getId()].updateStatus(status)

    def updatePriority(self, task, prio):
        self.taskList[task.getId()].updatePriority(prio)

    def updateDescription(self, task, des):
        self.taskList[task.getId()].updateDescription(des)

    def updateAssignee(self, task, user):
        self.taskList[task.getId()].updateAssignee(user)

    def removeTask(self, task):
        if task.getId() in self.taskList:
            del self.taskList[task.getId()]
            self.log.info(f"Task {task.getName()} has been deleted")
            return
        self.log.warning(f"Task {task.getId()} doesn't exist")

    def searchTask(self, id ):
        if id in self.taskList:
            return self.taskList[id].getTask()

        self.log.warning(f"Task with {id} doesn't exist")

    def filterWUser(self, assignee):
        #filters tasks which are assigned to user
        pass

    def filterWTime(self, time1, time2):
        # filters tasks which are in time range time1 and time2
        pass

    def filterWPriority(self, p):
        # filters tasks which have priority p
        pass

    def showHistory(self, user):
        flag = False
        for key,val in self.taskList.items():
            if val.getTask().getAssignee().getName() == user.getName():
                flag = True
                self.log.info(f"Task {key} was assigned to user {user.getName()}")
        if not flag:
            self.log.warning(f"No history found for user {user.getName()}")

    def remindUser(self,task):
        if task.getId() in self.taskList and self.taskList[task.getId()].getTask().getStatus() != Status.COMPELETED:
            self.taskList[task.getId()].getTask().remind()

