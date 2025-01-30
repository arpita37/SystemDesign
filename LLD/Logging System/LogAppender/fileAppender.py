from LogAppender.appenderInterface import LogAppender
from Message.logmessage import LogMessage

class FileAppender(LogAppender):
    def __init__(self, filepath : str):
        self.path = filepath

    def appendLog(self, message: LogMessage):
        with open(self.path,"a") as file:
            file.write(message.getMessage())
