import os
from pprint import pprint
import sys
import inquirer

from src.pages.compose import Compose
from src.models.incoming_mail import IncomingMail
from src.services.mail_service import MailService


class Home:
    def __init__(self, user):
        self.user = user
        self.select_menu()

    def select_menu(self):
        while True:
            os.system("cls")
            menu_options = [
                "Compose",
                "Refresh",
                "Exit",
                "------",
                "INBOX",
                "------",
            ]

            inbox = MailService.get_inbox()
            self.inbox_items = [
                f"{mail.sender[0]} \t {mail.received_date} \t\t  {mail.subject} - {mail.message}"
                for mail in inbox
            ]

            menu_options.extend(self.inbox_items)

            questions = [
                inquirer.List("menu", message="PYMAIL ALPHA: ", choices=menu_options)
            ]

            choices_index = menu_options.index(inquirer.prompt(questions)["menu"])
            pprint(choices_index)

            if choices_index == 1:
                continue

            if choices_index < 6:
                self.handle_menu_selection(choices_index)
            else:
                self.open_mail(inbox[choices_index - 6])

    def handle_menu_selection(self, selected_index):
        Compose(sender=self.user) if selected_index == 0 else None
        self.refresh_inbox if selected_index == 1 else None
        sys.exit(0) if selected_index == 2 else None

    def open_mail(self, mail: IncomingMail):
        os.system("cls")
        mail.show()

        questions = [inquirer.List("inbox", message="", choices=["Reply", "Back"])]

        if inquirer.prompt(questions)["inbox"] == "Reply":
            mail.reply(self.user, MailService)

    def refresh_inbox(self):
        raise StopIteration
