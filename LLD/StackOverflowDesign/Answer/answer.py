from datetime import datetime
from random import randint
from typing import List
from Comments.commentInterface import Commentable
from Question.question import Question
from User.user import User
from Votes.votableInterface import Votable
from Votes.vote import Vote


class Answer( Votable, Commentable):
    def __init__(self, text: str, question: Question, author: User):
        self.text = text
        self.associatedQuestion = question
        self.id = randint(0, 10000000)
        self.author = author
        self.creationDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.vote : List[Vote] = None
        self.comments = None

    def getAnswer(self):
        return self.text

    def getAnswerId(self):
        return self.id

    def getCreationDate(self):
        return self.creationDate

    def getVotes(self):
        return self.vote

    def getAuthor(self):
        return self.author

    def getAssociatedQuestion(self):
        return self.associatedQuestion

    def addVote(self, vote: Vote):
        for v in self.vote:
            if v.user.getUserID() == vote.user.getUserID():
                print(f"Already vote given to answer { self.getAnswerId()}")
                return
        self.vote.append(vote)

    def deleteVote(self, vote:Vote):
        for v in self.vote:
            if v.user == vote.user:
                self.vote.remove(v)
                print(f"Removed vote for user {vote.user.getUserID()}")
                return

        print(f"Could not find any vote given by user {vote.user.getUserID()}")

    def addComment(self, comment):
        self.comments.append(comment)

    def deleteComment(self, comment):
        for comm in self.comments:
            if comm.getCommentId() == comment.getCommentId():
                self.comments.remove(comm)
                print(f"Removed comment with Id {comment.getCommentId()}")
                return
        print(f"Could not find comment associated with answer {self.getAnswerId()}")

