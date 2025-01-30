from enum import Enum

class Loglevels(Enum):
    INFO: str = "INFO"
    DEBUG:str = "DEBUG"
    WARNING:str = "WARNING"
    ERROR:str = "ERROR"
    FATAL:str = "FATAL"