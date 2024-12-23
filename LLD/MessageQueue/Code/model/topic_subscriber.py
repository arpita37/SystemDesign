from typing import Final
from model.atomic_integer import AtomicInteger
from public_interface.isubscriber import ISubscriber
from threading import RLock

class TopicSubscriber:
    def __init__(self, subscriber:ISubscriber ,rlock : RLock):
        self.offset : AtomicInteger = 0 #assign final Attribute
        self.subscriber = subscriber
        self.rlock = rlock
        assert subscriber is not None

    def __call__( self, *args, **kwds ):
        """
        This method gets called before a method is called to sync access to the core object.
        """
        with self.rlock:
            rval = self.func(*args, **kwds)
            return rval

    def getOffset(self):
        return self.offset
    
    def getSubscriber(self):
        return self.subscriber
    
    def setOffset(self, val:int):
        if self.offset == val-1:
            self.offset = val