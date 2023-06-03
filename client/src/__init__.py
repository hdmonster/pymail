from src.models.mail import User
from src.services.mail_service import MailService
from src.pages.main import Home


name = input("Enter your name: ")
email = input("Enter your email: ")

MailService.setup_user(User(name, email))
MailService.start()

_ = Home(user=(name, email))
