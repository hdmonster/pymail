from src.services.mail_service import MailService
from src.models.mail_abs import Mail


class OutgoingMail(Mail):
    def __init__(self, sender, recipient, subject, message):
        super().__init__(sender, recipient)
        self.subject = subject
        self.message = message
