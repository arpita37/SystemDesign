from model import Topic, TopicSubscriber
import threading

class subscriberWorker:
    def __init__(self,topic:Topic, topicSubscriber : TopicSubscriber):
        self.topic = topic
        self.topicSubscriber = topicSubscriber
        self.condition = threading.Condition()

    def run(self):
        with self.condition:
            while(True):
                currOffset = self.topicSubscriber.getOffset()
                while( currOffset >= self.topic.getMessage().size()):
                    self.condition.sleep(10)
                msg = self.topic.getMessages()[currOffset]
                # We can't just increment here since subscriber offset can be reset it is consuming. 
                # So, after consuming we have to increase if it was previous one
                self.topicSubscriber.getSubscriber().setOffset(currOffset+1)

    def wakeUpIfNeeded(self):
        self.condition.notify()
