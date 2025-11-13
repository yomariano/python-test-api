from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from models import JobApplication, JobApplicationCreate, JobApplicationUpdate
from database import get_supabase

router = APIRouter(prefix="/job-applications", tags=["job-applications"])


@router.get("/", response_model=List[JobApplication])
async def get_job_applications(
    user_id: Optional[str] = Query(None),
    job_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
):
    """Get all job applications with optional filters"""
    try:
        query = get_supabase().table("job_applications").select("*")

        if user_id:
            query = query.eq("user_id", user_id)
        if job_id:
            query = query.eq("job_id", job_id)
        if status:
            query = query.eq("status", status)

        response = query.execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{application_id}", response_model=JobApplication)
async def get_job_application(application_id: str):
    """Get a specific job application by ID"""
    try:
        response = get_supabase().table("job_applications").select("*").eq("id", application_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job application not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=JobApplication, status_code=status.HTTP_201_CREATED)
async def create_job_application(application: JobApplicationCreate):
    """Create a new job application"""
    try:
        response = get_supabase().table("job_applications").insert(
            application.model_dump(exclude_unset=True)
        ).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{application_id}", response_model=JobApplication)
async def update_job_application(application_id: str, application: JobApplicationUpdate):
    """Update a job application"""
    try:
        response = get_supabase().table("job_applications").update(
            application.model_dump(exclude_unset=True)
        ).eq("id", application_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job application not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job_application(application_id: str):
    """Delete a job application"""
    try:
        response = get_supabase().table("job_applications").delete().eq("id", application_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job application not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
