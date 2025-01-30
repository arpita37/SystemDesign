from datetime import datetime
from Loglevels.logLevels import Loglevels

class LogMessage:
    def __init__(self, level : Loglevels, txt : str):
        self.time = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
        self.loglevel = level
        self.message = txt

    def getLogeLevel(self):
        return self.loglevel

    def getMessage(self):
        return f"\n[{self.loglevel.value}] {self.time} : {self.message}"

