from threading import Lock
import logging
from model.lisNode import ListNode

logging.basicConfig(level = logging.INFO)
class LRUCache:
    _instance = None

    def __new__(cls):
        cls._instance = super().__new__(cls)
        cls._instance.hashmap = dict()
        cls._instance.head = None
        cls._instance.tail = None
        cls._instance.capacity = 0
        cls._instance.maxCapacity = 0
        cls._instance.lock = Lock()
        cls._instance.log = logging.getLogger("LRUCache")
        return cls._instance

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            LRUCache()
        return cls._instance

    def setCapacity(self,num):
        self.maxCapacity = num

    def putKey(self,key,v):
        self.lock.acquire()
        flag = False
        if key in self.hashmap:
            self.hashmap[key][1] = v
            self.lock.release()
            self.getKey(key)
            self.log.info(f"Value {key} added successfully!!!")
            return
        if self.capacity == self.maxCapacity:
            flag = True
            node = self.head
            node.next.prev = None
            self.head = self.head.next
            node.next = None
            val = node.val
            self.hashmap.pop(val)
            self.capacity -= 1

        if not self.head:
            self.head = ListNode(key)
            self.tail = self.head
        else:
            node = ListNode(key)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.hashmap[key] = [self.tail,v]
        self.log.info(f"Value {key} added successfully!!!")
        if flag:
            self._printCache()
        self.capacity += 1
        self.lock.release()

    def getKey(self,val):
        self.lock.acquire()
        if val not in self.hashmap:
            self.log.info(f"The value {val} does not exist in the map")
            return
        node : ListNode = self.hashmap[val][0]
        if self.capacity != 1:
            if self.head == node:
                self.head = node.next
                node.next.prev = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                node.next = None
            else:
                if self.tail != node:
                    temp = node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    node.next = None
        self.log.info(f"The key {val} has been found")
        self._printCache()
        self.lock.release()

    def _printCache(self):
        temp = self.head
        while(temp):
            self.log.info(f"{temp.val}")
            temp = temp.next