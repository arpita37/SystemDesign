from random import randint


class Tag:
    def __init__(self, name : str):
        self.id = randint(0,1000000)
        self.name = name