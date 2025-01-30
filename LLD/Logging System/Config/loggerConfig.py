from LogAppender.appenderInterface import LogAppender
from Loglevels.logLevels import Loglevels


class LoggerConfig:
    def __init__(self, level : Loglevels, appender : LogAppender):
        self.level = level
        self.appender = appender

    def setLevel(self, level:Loglevels):
        self.level = level

    def getLevel(self):
        return self.level

    def setAppender(self, appender: LogAppender):
        self.appender = appender

    def getAppender(self):
        return self.appender