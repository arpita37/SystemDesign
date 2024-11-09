class Topic:
    def __init__(self,topicName="", topicID=0) -> None:
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
    
    def addMessage(self, messgae):
        self.messages.append(messgae)

    def addSubscriber(self, subsriber):
        self.subscribers.append(subsriber)


    ### We are not adding any setter for TopicdID and topicName because ideally they should not be changed
    ### once created.