import lib.socket
from services.mail_service import MailService

# print("Server is running")
# service = MailService()
# service.start()

while True:
    try:
        print("Server is running")
        service = MailService()
        service.start()
    except KeyboardInterrupt:
        service.stop()
    except Exception as e:
        print("Server crashed. Restarting...", e)
