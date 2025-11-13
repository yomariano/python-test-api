from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from models import SavedSearch, SavedSearchCreate, SavedSearchUpdate
from database import get_supabase

router = APIRouter(prefix="/saved-searches", tags=["saved-searches"])


@router.get("/", response_model=List[SavedSearch])
async def get_saved_searches(user_id: Optional[str] = Query(None)):
    """Get all saved searches, optionally filtered by user_id"""
    try:
        query = get_supabase().table("saved_searches").select("*")
        if user_id:
            query = query.eq("user_id", user_id)
        response = query.execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{search_id}", response_model=SavedSearch)
async def get_saved_search(search_id: str):
    """Get a specific saved search by ID"""
    try:
        response = get_supabase().table("saved_searches").select("*").eq("id", search_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Saved search not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=SavedSearch, status_code=status.HTTP_201_CREATED)
async def create_saved_search(search: SavedSearchCreate):
    """Create a new saved search"""
    try:
        response = get_supabase().table("saved_searches").insert(
            search.model_dump(exclude_unset=True)
        ).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{search_id}", response_model=SavedSearch)
async def update_saved_search(search_id: str, search: SavedSearchUpdate):
    """Update a saved search"""
    try:
        response = get_supabase().table("saved_searches").update(
            search.model_dump(exclude_unset=True)
        ).eq("id", search_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Saved search not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{search_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_saved_search(search_id: str):
    """Delete a saved search"""
    try:
        response = get_supabase().table("saved_searches").delete().eq("id", search_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Saved search not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
