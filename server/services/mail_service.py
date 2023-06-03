import ast
import threading
from typing import List


from models.mail import Mail
from models.user import User
from lib.socket import server


class MailService:
    def __init__(self):
        self.clients = []
        self.users: List[User] = []

    def broadcast(self, sender, message):
        for client in self.clients:
            if client != sender:
                client.send(message)

    def handle(self, client):
        while True:
            try:
                data = client.recv(1024)
                self.broadcast(sender=client, message=data)
                print(data)
            except Exception as e:
                print("handle error", e)
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                user = self.users[index]
                print("{} is offline".format(user.name))
                self.users.remove(user)
                break

    def start(self):
        while True:
            client, address = server.accept()
            print("Connected with {}".format(str(address)))

            client.send("USER".encode("ascii"))
            user_dict = client.recv(1024).decode("ascii")
            user_json = ast.literal_eval(user_dict)
            user = User.from_dict(user_json)

            self.users.append(user)
            self.clients.append(client)

            print("{} is online".format(user.name))
            self.broadcast(client, "{} is online".format(user.name).encode("ascii"))
            client.send("Connected to the server".encode("ascii"))

            thread = threading.Thread(target=self.handle, args=(client,))
            thread.daemon = True
            thread.start()
