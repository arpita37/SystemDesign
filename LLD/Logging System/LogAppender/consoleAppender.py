from LogAppender.appenderInterface import LogAppender
from Message.logmessage import LogMessage
class ConsoleAppender(LogAppender):
    def __init__(self):
        pass

    def appendLog(self, message : LogMessage):
        print(message.getMessage())
