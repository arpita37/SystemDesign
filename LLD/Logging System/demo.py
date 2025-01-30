from Config.loggerConfig import LoggerConfig
from LogAppender.fileAppender import FileAppender
from Loglevels.logLevels import Loglevels
from logger import Logger

class LoggerDemo:
    @staticmethod
    def run():
        logObj = Logger()
        logObj.getInstance()
        logObj.info("This is for a console message")
        logObj.warning("This is a waring for console")
        logObj.debug("This is a debug for console ")

        fileAppender = FileAppender("output.txt")
        logObj.loggerConfig = LoggerConfig(Loglevels.INFO,fileAppender)
        logObj.info("This is an info for text file")
        logObj.warning("This is an info for text file")
        logObj.debug("This is an info for text file")


if __name__ == "__main__":
    LoggerDemo.run()