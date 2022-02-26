import os

from dotenv import load_dotenv
from flask import Flask
from data import db_session
from data import __all_models
from data.users import User

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Sabelnikova"
    user.name = "Vlada"
    user.age = 17
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_2"
    user.email = "vlada@mars.org"
    user.hashed_password = "pass"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Ruzin"
    user.name = "Ivan"
    user.age = 77
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_3"
    user.email = "ruzin@mars.org"
    user.hashed_password = "pass_1"
    session.add(user)
    session.commit()

    user = User()
    user.surname = "Sidenko"
    user.name = "Oleg"
    user.age = 16
    user.position = "colonist"
    user.speciality = "research engineer"
    user.address = "module_4"
    user.email = "sidenko@mars.org"
    user.hashed_password = "pass_2"
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
