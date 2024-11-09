from collections import defaultdict
from typing import Final
from SystemDesign.LLD.MessageQueue.Code.handler import TopicHandler
from SystemDesign.LLD.MessageQueue.Code.model import Topic
from SystemDesign.LLD.MessageQueue.Code.model import TopicSubscriber
from SystemDesign.LLD.MessageQueue.Code.model.Message import Message
from SystemDesign.LLD.MessageQueue.Code.public_interface import ISubscriber
import random
import concurrent.futures
import threading

class Queue:
    def __init__(self):
        self.topicHandlers = defaultdict(TopicHandler)
        self.rlock = threading.RLock

    def createTopic(self, topicanme : Final str) -> Topic: # type: ignore
        topic : Final = Topic(topicanme, str(random.randint()))
        tHandler = TopicHandler(topic)
        self.topicHandlers[topic.getTopicId()] = tHandler
        print(f"Created the topic {topic.getTopicName()}")
        return topic

    def subscribe(self, subscriber : ISubscriber, topic :Topic):
        topic.addSubscriber(TopicSubscriber(subscriber,self.rlock))
        print(f"{subscriber.getId()} subscribed to the topic {topic.getTopicName()}")

    def publish(self, topic :Topic, message : Message): 
        topic.addMessage(message)
        print(f"{message} has been published to topic {topic}")
        tHandler = self.topicHandlers[topic.getTopicId()]
        with concurrent.futures.ThreadPoolExecutor as exec: ## Fanout message to the subcriber
            result = exec.submit(tHandler.publish)  ## new thread for publishing the topic
        

    def resetOffset(self, topic:Topic, subscriber : ISubscriber, newOffset : int):
        for sub in topic.getSubscribers():
            if sub.getSubscriber() == subscriber:
                sub.getOffset() = newOffset
                print(f"{sub.getSubscriber().getId()} offset reset to {newOffset}")
                tHandler = self.topicHandlers[topic.getTopicId()]
                t = threading.Thread(target=tHandler.startSubWorker,args=[subscriber])
                t.start()
                break