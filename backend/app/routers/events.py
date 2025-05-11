import json
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.events import Event
from app.schemas.events import EventResponse

router = APIRouter()


@router.get("/", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    parsed_events = []
    for event in events:
        parsed_events.append({
            **event.__dict__,
            "category_json": json.loads(event.category_json)
        })
    return parsed_events

@router.get("/{month}", response_model=List[EventResponse])
def get_month_events(month: int, db: Session = Depends(get_db)):
    events = db.query(Event).filter(Event.month == month).all()
    parsed_events = []
    for event in events:
        parsed_events.append({
            **event.__dict__,
            "category_json": json.loads(event.category_json)
        })
    return parsed_events



