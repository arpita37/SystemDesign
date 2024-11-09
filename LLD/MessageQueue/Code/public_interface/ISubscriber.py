from SystemDesign.LLD.MessageQueue.Code.model.Message import Message
class ISubscriber: ## This is an interface
    def __init__(self):
        pass

    def getId(self):
        pass

    def consume(self, message : Message):
        pass
