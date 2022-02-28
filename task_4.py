import os

from dotenv import load_dotenv
from flask import Flask
from data import db_session
from data import __all_models
from data.jobs import Jobs

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    session.add(job)
    session.commit()


if __name__ == '__main__':
    main()
