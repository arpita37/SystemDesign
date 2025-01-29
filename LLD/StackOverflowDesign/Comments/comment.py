from datetime import datetime
from random import randint
from User.user import User
from Votes.vote import Vote
from typing import List

class Comment:
    def __init__(self, text: str, author: User):
        self.text = text
        self.id = randint(0, 10000000)
        self.creationDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.vote : List[Vote] = None
        self.author = author

    def getComment(self):
        return self.text

    def getCommentId(self):
        return self.id

    def getCreationDate(self):
        return self.creationDate

    def getVotes(self):
        return self.vote

    def getAuthor(self):
        return self.author

    def addVote(self, vote: Vote):
        for v in self.vote:
            if v.user.getUserID() == vote.user.getUserID():
                print(f"Already vote given to answer {self.getAnswerId()}")
                return
        self.vote.append(vote)

    def deleteVote(self, vote: Vote):
        for v in self.vote:
            if v.user == vote.user:
                self.vote.remove(v)
                print(f"Removed vote for user {vote.user.getUserID()}")
                return

        print(f"Could not find any vote given by user {vote.user.getUserID()}")
