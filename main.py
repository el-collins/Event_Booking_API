from fastapi import FastAPI, HTTPException
from model import Attendee, EventDetails, TicketType


app = FastAPI()


def validate_attendee(attendee: Attendee):
    # Simulate attendee validation logic
    if len(attendee.name) < 2:
        raise HTTPException(status_code=400, detail="Name must be at least 2 characters long")
    if "@" not in attendee.email:
        raise HTTPException(status_code=400, detail="Invalid email address")
    if attendee.age < 18:
        raise HTTPException(status_code=400, detail="Attendee must be at least 18 years old")

@app.post("/book_event/")
async def book_event(attendee: Attendee):
    # Validate attendee
    validate_attendee(attendee)
    return {"message": "Attendee validated successfully"}



def validate_ticket_type(ticket_type: TicketType):
    # Simulate ticket type validation logic
    if ticket_type not in TicketType:
        raise HTTPException(status_code=400, detail="Invalid ticket type")

@app.post("/validate_ticket_type/")
async def validate_ticket(ticket_type: TicketType):
    # Validate ticket type
    validate_ticket_type(ticket_type)
    return {"message": "Ticket type validated successfully"}


def validate_event_details(event_details: EventDetails):
    # Simulate event details validation logic
    if len(event_details.name) < 5:
        raise HTTPException(status_code=400, detail="Event name must be at least 5 characters long")
    if len(event_details.location) < 5:
        raise HTTPException(status_code=400, detail="Event location must be at least 5 characters long")

@app.post("/validate_event_details/")
async def validate_event(event_details: EventDetails):
    # Validate event details
    validate_event_details(event_details)
    return {"message": "Event details validated successfully"}
