import sys
from sqlalchemy.orm.session import Session
from alphakill-tweebot.database.models import User, UserRole
from alphakill-tweebot.database.base import SessionLocal
from alphakill-tweebot.app import Application
from alphakill-tweebot.app.error import ApplicationError
from alphakill-tweebot.app.container import ApplicationContainer


def __create_admin_user(
    first_name: str,
    last_name: str,
    username: str,
    phonenumber: str,
    email: str,
    password: str,
):
    app: Application = ApplicationContainer.app()
    session: Session = SessionLocal()
    try:
        app.create_user(
            session,
            first_name,
            last_name,
            username,
            email,
            phonenumber,
            password,
            UserRole.ADMIN,
        )
        session.close()
    except ApplicationError as e:
        print(str(e))


def create_admin_user():
    first_name: str
    last_name: str
    email: str
    username: str
    phonenumber: str
    password: str
    if len(sys.argv) <= 1:
        # name = input("Admin Full Name: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        username = input("Enter username: ")
        email = input("Email Address: ")
        phonenumber = input("Enter Phonenumber: ")
        password = input("password: ")
    elif len(sys.argv) == 7:
        first_name = sys.argv[1]
        last_name = sys.argv[2]
        username = sys.argv[3]
        email = sys.argv[4]
        phonenumber = sys.argv[5]
        password = sys.argv[6]
    else:
        print(
            "\nError:\n run: poetry run create_admin_user [firstname] [lastname] [username] [email] [phonenumber] [password]"
        )
        return
    __create_admin_user(first_name, last_name, username, phonenumber, email, password)
    print(f"User with and email {email} successfully created")
