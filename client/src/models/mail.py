from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class User:
    name: str
    email: str

    @staticmethod
    def from_dict(obj: Any) -> "User":
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        email = from_str(obj.get("email"))
        return User(name, email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["email"] = from_str(self.email)
        return result


@dataclass
class Mail:
    sender: User
    recipient: User
    subject: str
    message: str

    @staticmethod
    def from_dict(obj: Any) -> "Mail":
        assert isinstance(obj, dict)
        sender = User.from_dict(obj.get("sender"))
        recipient = User.from_dict(obj.get("recipient"))
        subject = from_str(obj.get("subject"))
        message = from_str(obj.get("message"))
        return Mail(sender, recipient, subject, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["sender"] = to_class(User, self.sender)
        result["recipient"] = to_class(User, self.recipient)
        result["subject"] = from_str(self.subject)
        result["message"] = from_str(self.message)
        return result


def mail_from_dict(s: Any) -> Mail:
    return Mail.from_dict(s)


def mail_to_dict(x: Mail) -> Any:
    return to_class(Mail, x)
