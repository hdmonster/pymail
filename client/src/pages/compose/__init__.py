import os
import inquirer
from pprint import pprint

from src.services.mail_service import MailService
from src.models.mail import Mail, User


class Compose:
    def __init__(cls, sender):
        os.system("cls")
        cls.sender = sender
        cls.recipient = input("To: ")
        cls.subject = input("Subject: ")
        cls.message = input("Message:\n")

        confirm = [
            inquirer.Confirm(
                "send",
                message="Send mail to {}".format(cls.recipient),
                default=True,
            )
        ]

        answer = inquirer.prompt(confirm)
        pprint(answer)

        if answer["send"]:
            mail = Mail(
                sender=User(sender[0], sender[1]),
                recipient=User("", cls.recipient),
                subject=cls.subject,
                message=cls.message,
            )

            MailService.send(mail)
