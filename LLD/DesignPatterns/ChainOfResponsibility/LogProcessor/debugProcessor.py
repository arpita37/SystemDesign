from DesignPatterns.ChainOfResponsibility.LogLevels.levels import LogLevels
from DesignPatterns.ChainOfResponsibility.LogProcessor.logProcessorInterface import LogProcessor


class DebugProcessor(LogProcessor):
    def __init__(self, nextProcessor):
        super().__init__(nextProcessor)

    def log(self, level, message):
        if level == LogLevels.DEBUGGER:
            print("\nDebug : ", message)
        else:
            super().log(level, message)