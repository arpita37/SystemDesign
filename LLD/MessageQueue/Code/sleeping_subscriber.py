from typing import Final
from model.message import Message
from public_interface.isubscriber import ISubscriber
import threading

class SleepingSubscriber(ISubscriber):
    def __init__(self, id: int, sleepTimeInMillis: int):
        super().__init__()
        self.id= id
        self.sleepTimeInMillis = sleepTimeInMillis
        assert id is not None

    def getId(self):
        return self.id

    def consume(self,message:Message):
        print(f"Subscriber: {self.id} started consuming: {message.getMsg()}")
        threading.Thread.sleep(self.sleepTimeInMillis)
        print(f"Subscriber: {self.id} done consuming: { message.getMsg()}")