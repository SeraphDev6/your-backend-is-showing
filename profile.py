from typing import Literal, Optional
from sqlmodel import TEXT, Field, Relationship, SQLModel


class ProfileBase(SQLModel):
    name: str
    special_information: str = Field(sa_type=TEXT)
    requires_having_emergency: Optional[bool] = False


class Profile(ProfileBase, table=True):
    uid: str = Field(primary_key=True)
    contacts: list["Contact"] = Relationship(
        back_populates="profile", cascade_delete=True
    )
    having_emergency: bool = False

    @property
    def is_available(self) -> bool:
        if self.requires_having_emergency:
            return self.having_emergency
        return True


class ProfileRead(ProfileBase):
    uid: str
    contacts: list["ContactRead"]
    having_emergency: bool


class EmergencyRequest(SQLModel):
    emergency_status: Literal["Emergency", "All Clear"]

    @property
    def bool_status(self) -> bool:
        return self.emergency_status == "Emergency"


from api.models.contact import Contact, ContactRead
