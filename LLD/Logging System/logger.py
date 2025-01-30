from Config.loggerConfig import LoggerConfig
from LogAppender.consoleAppender import ConsoleAppender
from Loglevels.logLevels import Loglevels
from Message.logmessage import LogMessage


class Logger:
    _instance = None

    def Logging(self):
        if self._instance != None:
            print("Logger is a singleton class")
        else:
            self._instance = self
            self.loggerConfig = LoggerConfig(Loglevels.INFO, ConsoleAppender())
        return self._instance

    def getInstance(self):
        self.Logging()

    def log(self,level,message):
        logMessage = LogMessage(level, message)
        self.loggerConfig.getAppender().appendLog(logMessage)

    def debug(self, message):
        self.log(Loglevels.DEBUG, message)

    def info(self, message):
        self.log(Loglevels.INFO, message)

    def warning(self, message):
        self.log(Loglevels.WARNING, message)

    def error(self, message):
        self.log(Loglevels.ERROR, message)

    def fatal(self, message):
        self.log(Loglevels.FATAL, message)