import ast
from datetime import datetime
import threading
from time import sleep
from lib.socket import client

from src.utils.date_formatter import minimal_date
from src.models.mail import Mail, User
from src.models.incoming_mail import IncomingMail


class MailService:
    user: User = None
    mails = []

    @classmethod
    def setup_user(cls, user):
        cls.user = user

    @classmethod
    def receive(cls):
        while True:
            try:
                message = client.recv(1024).decode("ascii")
                print(message)
                if message == "USER":
                    client.send(f"{cls.user.to_dict()}".encode("ascii"))
                else:
                    if message[0] is not "{":
                        continue

                    mail_dict = ast.literal_eval(message)
                    mail = Mail.from_dict(mail_dict)

                    if mail.recipient.email == cls.user.email:
                        cls.mails.append(mail)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print("An error occurred", e)
                client.close()
                break

    @classmethod
    def send(cls, mail: Mail):
        client.send(str(mail.to_dict()).encode("ascii"))
        print("Message sent!")
        sleep(2)

    @classmethod
    def get_inbox(cls):
        inbox = []

        for mail in cls.mails:
            inbox.append(
                IncomingMail(
                    sender=(mail.sender.name, mail.sender.email),
                    recipient=(mail.recipient.name, mail.recipient.email),
                    subject=mail.subject,
                    message=mail.message,
                    received_date=minimal_date(datetime.today()),
                )
            )

        return inbox

    @classmethod
    def start(cls):
        thread = threading.Thread(target=cls.receive)
        thread.daemon = True
        thread.start()
