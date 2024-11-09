from collections import defaultdict
from typing import Final
from model.topic_subscriber import TopicSubscriber
from model.topic import Topic
from handler.subscriber_worker import SubscriberWorker
import threading

class TopicHandler:
    def __init__(self, topic : Topic=None ):
        self.topic = topic
        self.subsWorkers = defaultdict(SubscriberWorker)


    def publish(self):
        for subscriber in self.topic.getSubscribers():
            self.startSubWorkers(subscriber)


    def startSubWorker(self, topicSubscriber:TopicSubscriber):
        if topicSubscriber == None:
            raise IOError
        subId = topicSubscriber.getSubscriber().getId()
        if not self.subsWorkers.__contains__(subId): #Lazy creation, not created until required
            subWorker = SubscriberWorker(self.topic, topicSubscriber)
            self.subWorkers[subId] = subWorker
            t = threading.Thread(target=subWorker.run,args=topicSubscriber)
            t.start()
        subWorker : Final = self.subsWorkers.get(subId)
        subWorker.wakeUpIfNeeded()