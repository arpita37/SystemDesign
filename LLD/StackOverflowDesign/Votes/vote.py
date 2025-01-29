from User.user import User

class Vote:
    def __init__(self, user:User, value : int=1):
        self.user = user
        self.value = value