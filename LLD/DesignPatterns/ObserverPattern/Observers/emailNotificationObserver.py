from DesignPatterns.ObserverPattern.Observers.observerInterface import ObserverInterface


class EmailNotificationObserver(ObserverInterface):
    def __init__(self, email: str, username: str) -> None:
        super().__init__(username)
        self.email = email

    def update(self):
        self._sendMessageOnEmail(self.username, "Hurry up! iPhone stock is avaialable")

    def _sendMessageOnEmail(self, username: str, message: str) -> str:
        print(f"This is email notification for user {username}. {message}")
