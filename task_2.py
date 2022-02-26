class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    def __str__(self):
        return f'{self.team_leader} {self.job} {self.work_size}' \
               f' {self.collaborators} {self.is_finished}'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True
    )

    job = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    work_size = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=True
    )

    collaborators = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True
    )

    start_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        nullable=True,
        default=datetime.datetime.now
    )
    end_date = sqlalchemy.Column(
        sqlalchemy.DateTime
    )

    is_finished = sqlalchemy.Column(
        sqlalchemy.Boolean
    )

    team_leader = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey("users.id")
    )
    user = orm.relation('User')
