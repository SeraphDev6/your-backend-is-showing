import os
from sqlmodel import SQLModel, Session, create_engine
from .profile import *
from .contact import *

if "DATABASE_URL" in os.environ:
    print(os.getenv("DATABASE_URL"))
    url = os.getenv("DATABASE_URL").replace("postgres://", "postgresql://")
else:
    url = f""

engine = create_engine(
    url,
    pool_pre_ping=True,
    pool_recycle=3600,
    # connect_args={
    #     "keepalives": 1,
    #     "keepalives_idle": 30,
    #     "keepalives_interval": 10,
    #     "keepalives_count": 5,
    # },
)


def get_session():
    with Session(engine) as session:
        yield session


def create_db(drop: bool = False):
    if drop:
        SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
