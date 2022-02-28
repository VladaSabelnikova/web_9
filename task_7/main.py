import os

from dotenv import load_dotenv
from flask import Flask, render_template
from data import db_session
from data import __all_models
from data.jobs import Jobs
from task_7.data.users import User

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def create_db_content(session):
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

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2'
    job.is_finished = False
    session.add(job)
    session.commit()

    job = Jobs()
    job.team_leader = 2
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 4'
    job.is_finished = False
    session.add(job)
    session.commit()

    job = Jobs()
    job.team_leader = 3
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 4, 5'
    job.is_finished = False
    session.add(job)
    session.commit()

    job = Jobs()
    job.team_leader = 3
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 4, 5'
    job.is_finished = False
    session.add(job)
    session.commit()


@app.route("/")
def index():
    jobs = session.query(Jobs)
    return render_template("index.html", jobs=jobs)


def main():
    app.run(host='localhost', port=5000)


db_session.global_init("db/blogs.db")
session = db_session.create_session()
create_db_content(session)


if __name__ == '__main__':
    main()
