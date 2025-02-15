from publicInterface.lruCache import LRUCache


class Demo:
    @staticmethod
    def run():
        obj = LRUCache()
        obj.getInstance()
        obj.setCapacity(5)
        obj.putKey(1,2)
        obj.putKey(2, 3)
        obj.putKey(2, 4)
        obj.putKey(4, 5)
        obj.putKey(5, 6)
        obj.getKey(5)
        obj.getKey(2)
        obj.getKey(1)
        obj.putKey(8, 6)

if __name__ == "__main__":
    Demo.run()