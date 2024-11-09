from model.topic_subscriber import TopicSubscriber
from model.message import Message


class Topic:
    def __init__(self,topicName : str="", topicID : int=0) -> None:
        self.topicName = topicName
        self.topicID = topicID
        self.messages = list() ## Message type
        self.subscribers = list() ##TopicSubscriber type

    def getTopicId(self):
        return self.topicID
    def getTopicName(self):
        return self.topicName
    def getMessages(self):
        return self.messages
    
    def getSubscribers(self):
        return self.subscribers
    
    def addMessage(self, messgae:Message):
        self.messages.append(messgae)

    def addSubscriber(self, subsriber: TopicSubscriber):
        self.subscribers.append(subsriber)


    ### We are not adding any setter for TopicdID and topicName because ideally they should not be changed
    ### once created.