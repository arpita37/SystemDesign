from threading import Lock
from typing import List
from Answer.answer import Answer
from Comments.comment import Comment
from Comments.commentInterface import Commentable
from Question.question import Question
from User.user import User
import logging

class StackOverflow:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            cls._instance = super().__new__(cls)
            cls._users: List[User] = []
            cls._questions: List[Question] = []
            cls._answers: List[Answer] = []
            cls._log = logging.getLogger("Log")
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance:
            print(f"This is a singleton class. Can't be instantiated again.")
        return cls._instance

    def addUser(self, usr : User):
        for u in self._users:
            if u.getUserID() == usr.getUserID():
                self._log.info("User already exists")
            return
        self._users.append((usr))
        self._log.info("User added successfully")

    def removeUser(self, usr : User):
        #delete answers
        for ans in self._answers:
            if ans.getAuthor().getUserID() == usr.getUserID():
                self.removeAnswer(ans)
        #delete questions
        for ques in self._questions:
            if ans.getAuthor().getUserID() == usr.getUserID():
                self.removeQuestion(ques)
        #delete user
        for user in self._users:
            if user.getUserID() == usr.getUserID():
                self._users.remove(user)
        self._log.info("User removed!!!")

    def addQuestion(self, ques: Question):
        self._questions.append(ques)
        self._log.info("Question added")

    def removeQuestion(self,ques: Question):
        for ans in self._answers:
            if ans.getAssociatedQuestion().getQuestionId() == ques.getQuestionId():
                self.removeAnswer(ans)

        for q in self._questions:
            if q.getQuestionId() == ques.getQuestionId():
                self._questions.remove((q))
        self._log.info("Question removed!!!")

    def addAnswer(self, ans : Answer):
        self._answers.append(ans)
        self._log.info("Answer added!!!")

    def removeAnswer(self, ans : Answer):
        for an in self._answers:
            if an.getAnswerId() == ans.getAnswerId():
                self._answers.remove(an)
                self._log.info("Answer deleted!!!")
                return
        self._log.warning("Answer doesn't exist")

    def displayQuestions(self):
        if not len(self._questions):
            self._log.info("No questions found")
            return
        for q in self._questions:
            print(f"\n{q.getQuestion()}\t{q.getQuestionId()}\t{q.getComments()}")

    def search_questions(self, query):
        return [q for q in self._questions if
                query.lower() in q.getQuestion().lower() or
                any(query.lower() == tag.name.lower() for tag in q.getTags())]

    def addComment(self,user:User, cmt : Comment, commentable:Commentable,):
        user.comment_on(commentable,cmt)