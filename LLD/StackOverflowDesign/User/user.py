from datetime import datetime
from numpy.random import randint


class User:
    def __init__(self,name : str, email : str):
        self.id = randint(0,100000000)
        self.name = name
        self.email = email
        self.reputation = 0
        self.creationDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    def getUserID(self):
        return self.id

    def getUserName(self):
        return self.name

    def getUserEmail(self):
        return self.email

    def getReputation(self):
        return self.reputation

    def getCreationDate(self):
        return self.creationDate

    def comment_on(self, commentable, comment):
        commentable.addComment(comment)
        self.update_reputation(2)  # Gain 2 reputation for commenting
        return comment

    def update_reputation(self, value):
        self.reputation += value
        self.reputation = max(0, self.reputation)  # Ensure reputation doesn't go below 0