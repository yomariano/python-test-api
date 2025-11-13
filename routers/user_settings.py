from fastapi import APIRouter, HTTPException, status
from typing import List
from models import UserSettings, UserSettingsCreate, UserSettingsUpdate
from database import get_supabase

router = APIRouter(prefix="/user-settings", tags=["user-settings"])


@router.get("/", response_model=List[UserSettings])
async def get_all_user_settings():
    """Get all user settings"""
    try:
        response = get_supabase().table("user_settings").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{user_id}", response_model=UserSettings)
async def get_user_settings(user_id: str):
    """Get user settings by user ID"""
    try:
        response = get_supabase().table("user_settings").select("*").eq("user_id", user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User settings not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=UserSettings, status_code=status.HTTP_201_CREATED)
async def create_user_settings(settings: UserSettingsCreate):
    """Create user settings"""
    try:
        response = get_supabase().table("user_settings").insert(
            settings.model_dump(exclude_unset=True)
        ).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{user_id}", response_model=UserSettings)
async def update_user_settings(user_id: str, settings: UserSettingsUpdate):
    """Update user settings"""
    try:
        response = get_supabase().table("user_settings").update(
            settings.model_dump(exclude_unset=True)
        ).eq("user_id", user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User settings not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_settings(user_id: str):
    """Delete user settings"""
    try:
        response = get_supabase().table("user_settings").delete().eq("user_id", user_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="User settings not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
