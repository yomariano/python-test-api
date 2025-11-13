from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from models import CV, CVCreate, CVUpdate
from database import get_supabase

router = APIRouter(prefix="/cvs", tags=["cvs"])


@router.get("/", response_model=List[CV])
async def get_cvs(user_id: Optional[str] = Query(None)):
    """Get all CVs, optionally filtered by user_id"""
    try:
        query = get_supabase().table("cvs").select("*")
        if user_id:
            query = query.eq("user_id", user_id)
        response = query.execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{cv_id}", response_model=CV)
async def get_cv(cv_id: str):
    """Get a specific CV by ID"""
    try:
        response = get_supabase().table("cvs").select("*").eq("id", cv_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="CV not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=CV, status_code=status.HTTP_201_CREATED)
async def create_cv(cv: CVCreate):
    """Create a new CV"""
    try:
        response = get_supabase().table("cvs").insert(cv.model_dump(exclude_unset=True)).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{cv_id}", response_model=CV)
async def update_cv(cv_id: str, cv: CVUpdate):
    """Update a CV"""
    try:
        response = get_supabase().table("cvs").update(
            cv.model_dump(exclude_unset=True)
        ).eq("id", cv_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="CV not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{cv_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cv(cv_id: str):
    """Delete a CV"""
    try:
        response = get_supabase().table("cvs").delete().eq("id", cv_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="CV not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
