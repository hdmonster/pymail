from abc import ABC


class Mail(ABC):
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
