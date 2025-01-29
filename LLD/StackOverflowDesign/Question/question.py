from random import random, randint
from typing import List, Set
from datetime import datetime

from Comments.commentInterface import Commentable
from Tags.tag import Tag
from User.user import User
from Votes.votableInterface import Votable
from Votes.vote import Vote


class Question(Votable, Commentable):
    def __init__(self, text: str, author : User):
        self.text = text
        self.id = randint(0,10000000)
        self.author = author
        self.creationDate = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.tag : Set[Tag] = set()
        self.vote: List[Vote] = []
        self.comments= []

    def getQuestion(self):
        return self.text

    def getQuestionId(self):
        return self.id

    def getTags(self):
        if not len(self.tag):
            print(f"\nNo tag found for question id {self.getQuestionId()}")
            return

        for t in self.tag:
            print(t.name,end=" ")

    def getComments(self):
        if not len(self.comments):
            print(f"\nNo tag found for question id {self.getQuestionId()}")
            return

        for t in self.comments:
            print(t.getComment(), end=" ")

    def getCreationDate(self):
        return self.creationDate

    def getVotes(self):
        if not len(self.vote):
            print(f"\nNo vote found for question id {self.getQuestionId()}")
            return
        likes = dislikes = 0
        for v in self.vote:
            if v.value >= 0 :
                likes += 1
            else:
                dislikes -= 1
        print(f"\nLikes:{likes}\tDislikes:{dislikes}")
        return

    def getAuthor(self):
        return self.author

    def addVote(self, vote: Vote):
        for v in self.vote:
            if v.user.getUserID() == vote.user.getUserID():
                print(f"\nAlready vote given to answer {self.getAnswerId()}")
                return
        self.vote.append(vote)

    def deleteVote(self, vote: Vote):
        for v in self.vote:
            if v.user == vote.user:
                self.vote.remove(v)
                print(f"\nRemoved vote for user {vote.user.getUserID()}")
                return

        print(f"\nCould not find any vote given by user {vote.user.getUserID()}")

    def addComment(self, comment):
        self.comments.append(comment)

    def deleteComment(self, comment):
        for comm in self.comments:
            if comm.getCommentId() == comment.getCommentId():
                self.comments.remove(comm)
                print(f"\nRemoved comment with Id {comment.getCommentId()}")
                return
        print(f"\nCould not find comment associated with question {self.getQuestionId()}")

    def addTag(self, tag:Tag):
        self.tag.add(tag)
        print(f"\nAdded tag with id {tag.id}")

    def removeTag(self, tag:Tag):
        if tag in self.tag:
            self.tag.remove(tag)
            print(f"\nRemoved tag with id {tag.id}")
