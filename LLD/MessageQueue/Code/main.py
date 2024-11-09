import time
from typing import Final
from sleeping_subscriber import SleepingSubscriber
from model.message import Message
from public_interface.mqueue import Queue


def Main():
        queue : Final = Queue()
        topic1: Final = queue.createTopic("t1")
        topic2: Final = queue.createTopic("t2")
        sub1 : Final= SleepingSubscriber("sub1", 10000)
        sub2 : Final = SleepingSubscriber("sub2", 10000)
        
        queue.subscribe(sub1, topic1)
        queue.subscribe(sub2, topic1)

        sub3 : Final = SleepingSubscriber("sub1", 5000)
        queue.subscribe(sub3, topic2)

        queue.publish(topic1, Message("m1"))
        queue.publish(topic1, Message("m2"))

        queue.publish(topic2, Message("m3"))

        time.sleep(15000)
        queue.publish(topic2, Message("m4"))
        queue.publish(topic1, Message("m5"))

        queue.resetOffset(topic1, sub1, 0)


if __name__=="__main__":
        Main()

        