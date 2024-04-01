from typing import Annotated
from pydantic import BaseModel, Field, StringConstraints
from enum import Enum

class Attendee(BaseModel):
    name: Annotated[str, StringConstraints(max_length=100)]
    email:  Annotated[str, StringConstraints(max_length=100)]
    age: Annotated[int, Field(gt=0)]



class TicketType(str, Enum):
    VIP = "VIP"
    General_Admission = "General Admission"

class EventDetails(BaseModel):
    name: Annotated[str, StringConstraints(max_length=100)]
    date: Annotated[str, StringConstraints(pattern=r"^\d{4}-\d{2}-\d{2}$")]
    location: Annotated[str, StringConstraints(max_length=100)]
    ticket_types: dict[TicketType, int]