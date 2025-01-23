from DesignPatterns.ChainOfResponsibility.LogLevels.levels import LogLevels
from DesignPatterns.ChainOfResponsibility.LogProcessor.logProcessorInterface import LogProcessor


class WarningProcessor(LogProcessor):
    def __init__(self, nextProcessor):
        super().__init__(nextProcessor)

    def log(self, level, message):
        if level == LogLevels.WARNING:
            print("\nWarning : ", message)
        else:
            super().log(level, message)