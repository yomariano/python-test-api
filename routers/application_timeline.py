from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from models import ApplicationTimeline, ApplicationTimelineCreate, ApplicationTimelineUpdate
from database import get_supabase

router = APIRouter(prefix="/application-timeline", tags=["application-timeline"])


@router.get("/", response_model=List[ApplicationTimeline])
async def get_application_timeline_events(
    application_id: Optional[str] = Query(None),
    event_type: Optional[str] = Query(None),
):
    """Get all application timeline events with optional filters"""
    try:
        query = get_supabase().table("application_timeline").select("*")

        if application_id:
            query = query.eq("application_id", application_id)
        if event_type:
            query = query.eq("event_type", event_type)

        response = query.order("created_at", desc=True).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{event_id}", response_model=ApplicationTimeline)
async def get_application_timeline_event(event_id: str):
    """Get a specific timeline event by ID"""
    try:
        response = get_supabase().table("application_timeline").select("*").eq("id", event_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Timeline event not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=ApplicationTimeline, status_code=status.HTTP_201_CREATED)
async def create_application_timeline_event(event: ApplicationTimelineCreate):
    """Create a new timeline event"""
    try:
        response = get_supabase().table("application_timeline").insert(
            event.model_dump(exclude_unset=True)
        ).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{event_id}", response_model=ApplicationTimeline)
async def update_application_timeline_event(event_id: str, event: ApplicationTimelineUpdate):
    """Update a timeline event"""
    try:
        response = get_supabase().table("application_timeline").update(
            event.model_dump(exclude_unset=True)
        ).eq("id", event_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Timeline event not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_application_timeline_event(event_id: str):
    """Delete a timeline event"""
    try:
        response = get_supabase().table("application_timeline").delete().eq("id", event_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Timeline event not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
