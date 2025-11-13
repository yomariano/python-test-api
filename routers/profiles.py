from fastapi import APIRouter, HTTPException, status
from typing import List
from models import Profile, ProfileCreate, ProfileUpdate
from database import get_supabase

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/", response_model=List[Profile])
async def get_profiles():
    """Get all profiles"""
    try:
        response = get_supabase().table("profiles").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{profile_id}", response_model=Profile)
async def get_profile(profile_id: str):
    """Get a specific profile by ID"""
    try:
        response = get_supabase().table("profiles").select("*").eq("id", profile_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Profile, status_code=status.HTTP_201_CREATED)
async def create_profile(profile: ProfileCreate):
    """Create a new profile"""
    try:
        response = get_supabase().table("profiles").insert(profile.model_dump(exclude_unset=True)).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{profile_id}", response_model=Profile)
async def update_profile(profile_id: str, profile: ProfileUpdate):
    """Update a profile"""
    try:
        response = get_supabase().table("profiles").update(
            profile.model_dump(exclude_unset=True)
        ).eq("id", profile_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(profile_id: str):
    """Delete a profile"""
    try:
        response = get_supabase().table("profiles").delete().eq("id", profile_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
