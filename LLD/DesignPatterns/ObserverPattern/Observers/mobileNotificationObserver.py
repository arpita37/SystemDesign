from DesignPatterns.ObserverPattern.Observers.observerInterface import ObserverInterface


class MobileNotificationObserver(ObserverInterface):
    def __init__(self, number : int, username : str) -> None:
        super().__init__(username)
        self.number = number

    def update(self):
        self._sendMessageOnMobile(self.username, "Hurry up! iPhone stock is avaialable")

    def _sendMessageOnMobile(self, username : str, message : str) -> str:
        print(f"This is mobile notification for user {username}. {message}")
