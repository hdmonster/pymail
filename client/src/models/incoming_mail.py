from src.models.mail import User, Mail
from src.models.mail_abs import Mail as MailAbs


class IncomingMail(MailAbs):
    def __init__(self, sender, recipient, subject, message, received_date):
        super().__init__(sender, recipient)
        self.subject = subject
        self.message = message
        self.received_date = received_date

    def show(self):
        print(f"From: {self.sender[0]} <{self.sender[1]}> \t\t\t {self.received_date}")
        print(f"Subject: {self.subject}")
        print("Message:")
        print(f"{self.message}")
        print("\n")

    def reply(self, user, mail_service):
        print("Replying to {}".format(self.sender[1]))
        message = input("")

        mail = Mail(
            sender=User(user[0], user[1]),
            recipient=User(self.sender[0], self.sender[1]),
            subject=self.subject,
            message=message,
        )

        mail_service.send(mail)
