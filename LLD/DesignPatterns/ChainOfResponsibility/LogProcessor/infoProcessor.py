from DesignPatterns.ChainOfResponsibility.LogLevels.levels import LogLevels
from DesignPatterns.ChainOfResponsibility.LogProcessor.logProcessorInterface import LogProcessor


class InfoProcessor(LogProcessor):
    def __init__(self, nextProcessor):
        super().__init__(nextProcessor)

    def log(self, level, message):
        if level == LogLevels.INFO:
            print("\nInfo : ", message)
        else:
            super().log(level, message)