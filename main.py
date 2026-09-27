import os
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import model_validator
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(override=True)
app = FastAPI(title="Test API")


class UserBase(SQLModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords Must match")
        return self


class User(UserBase, table=True):
    id: int = Field(primary_key=True)
    password: str


engine = create_engine(
    os.getenv("DATABASE_URL"),
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


create_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/users")
async def get_users(db: Session = Depends(get_session)) -> list[User]:
    """
    Gets a list of all existing users, with their password. Enjoy Hackers!
    """
    users = db.exec(select(User)).all()
    return users


@app.post("/users")
async def create_users(user: UserCreate, db: Session = Depends(get_session)) -> User:
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# if __name__ == "__main":
#     ""
