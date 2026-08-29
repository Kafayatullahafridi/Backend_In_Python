from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")