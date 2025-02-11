import uuid
from threading import Lock

class UserHandler:
    def __init__(self):
        self.userList  = dict()
        self.lock = Lock()

    def showUser(self):
        for key,val in self.userList.items():
            print(f"\nUserID: {key}\tUSerName:{val.getName()}")

    def createUser(self, user, log):
        self.lock.acquire(True, 100)
        if user.getId() not in self.userList:
            user.setId(self._generateUserId(user))
            self.userList[user.getId()] = user
            log.info(f"\nUser {user.getName()} ")
        else:
            log.warning(f"\nUser {user.getId()} already exists")
        self.lock.release()

    def removeUser(self, user, log):
        with self.lock:
            if user.getId() not in self.userList:
                log.warning(f"\nUser {user.getId()} does not exist")
                return
            self.userList.pop(user.getId())
            log.info(f"\nUser {user.getId()} has been deleted")

    def userExists(self,id):
        if id in self.userList:
            return True
        return False

    def getUser(self,id):
        return self.userList[id]

    def showHistory(self, user, log):
        try:
            userId = user.getId()
            obj = self.userList[userId]
            obj.viewTransactionHistory()
        except Exception as e:
            log.info(f"Some error occured: \n {e}")

    def checkBalance(self, userId, log):
        try:
            obj = self.userList[userId]
            amount = obj.getAmount()
            log.info(f"The total amount available is {amount}")
            return amount
        except Exception as e:
            raise ValueError(f"Could not get total balance, some error occured : {e}")
        return 0

    def _generateUserId(self,user):
        return f"{uuid.uuid4().hex[8]}_{user.getName()}"

