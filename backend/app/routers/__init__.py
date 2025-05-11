from fastapi import APIRouter

from app.routers import events

router = APIRouter()

router.include_router(events.router, prefix="/events", tags=["events"]) 