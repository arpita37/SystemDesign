from typing import Final
from SystemDesign.LLD.MessageQueue.Code.model.Message import Message
from SystemDesign.LLD.MessageQueue.Code.public_interface import ISubscriber
import threading

class SleepingSubscriber(ISubscriber):

    def __init__(self, id, sleepTimeInMillis):
        self.id : Final= id
        self.sleepTimeInMillis = sleepTimeInMillis
        assert id is not None

    def getId(self):
        return self.id

    def consume(self,message:Message):
        print(f"Subscriber: {self.id} started consuming: {message.getMsg()}")
        threading.Thread.sleep(self.sleepTimeInMillis)
        print(f"Subscriber: {self.id} done consuming: { message.getMsg()}")