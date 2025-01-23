from DesignPatterns.ChainOfResponsibility.LogLevels.levels import LogLevels
from DesignPatterns.ChainOfResponsibility.LogProcessor.debugProcessor import DebugProcessor
from DesignPatterns.ChainOfResponsibility.LogProcessor.errorProcessor import ErrorProcessor
from DesignPatterns.ChainOfResponsibility.LogProcessor.infoProcessor import InfoProcessor
from DesignPatterns.ChainOfResponsibility.LogProcessor.warningProcessor import WarningProcessor


def main():
    logObj = InfoProcessor( DebugProcessor ( WarningProcessor ( ErrorProcessor( None ))))
    logObj.log(LogLevels.ERROR, "This is for error message")
    logObj.log(LogLevels.INFO, "This is for info message")
    logObj.log(LogLevels.WARNING, "This is for warning message")
    logObj.log(LogLevels.DEBUGGER, "This is for debug message")


if __name__ == "__main__":
    main()