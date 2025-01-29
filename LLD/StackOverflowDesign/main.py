from psutil import users

from Comments.comment import Comment
from Question.question import Question
from StackOverflow.stackoverflow import StackOverflow
from User.user import User


class StackOverflowDemo:

    @staticmethod
    def run():
        SOObj = StackOverflow()
        user1 = User("Arpita", "arpitabasak031296@gmail.com")
        SOObj.addUser(user1)
        Q1 = Question("Who is the best footballplayer?",user1)
        SOObj.addQuestion(Q1)
        SOObj.displayQuestions()
        cmt1 = Comment("What are you taling about, it's always Messy!", user1)
        SOObj.addComment(user1,cmt1,Q1)
        SOObj.displayQuestions()

if __name__ == "__main__":
    StackOverflowDemo.run()