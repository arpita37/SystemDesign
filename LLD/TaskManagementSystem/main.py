import datetime

from Handlers.taskManagementSystem import TaskManagement
from Models.task import Task
from Models.user import User


class Demo:
    @staticmethod
    def run():
        #instace of taskmanager class
        taskManager = TaskManagement()
        taskManager.get_instance()

        #creating and adding user
        user1 = User("Arpita", "arpitabasak031296@gmail.com")
        user2 = User("Kingshuk", "kingshuk.basu91@yahoo.com")
        user3 = User("Adhrit", "adhrit.kar@gamil,com")
        taskManager.addUser(user1)
        taskManager.addUser(user2)
        taskManager.addUser(user3)

        #creating and adding task
        task1 = Task("Task 1", "Does type1 task",
                     datetime.datetime.today() + datetime.timedelta(days=5), owner=user1,
                     assignedTo=user3)
        taskManager.addTask(task1)
        taskManager.updateTime(task1,datetime.datetime.today() + datetime.timedelta(days=10))
        taskManager.showHistory(user3)
if __name__ == "__main__":
    Demo.run()
