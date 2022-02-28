class Department(SqlAlchemyBase):
    __tablename__ = 'department'

    def __str__(self):
        return f'{self.title} {self.members} {self.email} {self.chief}'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )

    title = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    members = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    email = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    chief = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id")
    )
    user = orm.relation('User')
