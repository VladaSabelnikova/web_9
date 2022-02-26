class User(SqlAlchemyBase):
    __tablename__ = 'users'

    def __str__(self):
        return f'{self.name} {self.email}'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )

    surname = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )

    name = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )

    age = sqlalchemy.Column(
        sqlalchemy.Integer, nullable=True
    )

    position = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )

    speciality = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )

    address = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )

    email = sqlalchemy.Column(
        sqlalchemy.String, unique=True, nullable=True
    )
    hashed_password = sqlalchemy.Column(
        sqlalchemy.String, nullable=True
    )
    modified_date = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.datetime.now
    )
