from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")
