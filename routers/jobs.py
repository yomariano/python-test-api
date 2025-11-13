from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from models import Job, JobCreate, JobUpdate
from database import get_supabase

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=List[Job])
async def get_jobs(
    user_id: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    job_type: Optional[str] = Query(None),
    is_remote: Optional[bool] = Query(None),
    status: Optional[str] = Query(None),
):
    """Get all jobs with optional filters"""
    try:
        query = get_supabase().table("jobs").select("*")

        if user_id:
            query = query.eq("user_id", user_id)
        if company:
            query = query.ilike("company", f"%{company}%")
        if location:
            query = query.ilike("location", f"%{location}%")
        if job_type:
            query = query.eq("job_type", job_type)
        if is_remote is not None:
            query = query.eq("is_remote", is_remote)
        if status:
            query = query.eq("status", status)

        response = query.execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{job_id}", response_model=Job)
async def get_job(job_id: str):
    """Get a specific job by ID"""
    try:
        response = get_supabase().table("jobs").select("*").eq("id", job_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=Job, status_code=status.HTTP_201_CREATED)
async def create_job(job: JobCreate):
    """Create a new job"""
    try:
        response = get_supabase().table("jobs").insert(job.model_dump(exclude_unset=True)).execute()
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{job_id}", response_model=Job)
async def update_job(job_id: str, job: JobUpdate):
    """Update a job"""
    try:
        response = get_supabase().table("jobs").update(
            job.model_dump(exclude_unset=True)
        ).eq("id", job_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job not found")
        return response.data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_job(job_id: str):
    """Delete a job"""
    try:
        response = get_supabase().table("jobs").delete().eq("id", job_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Job not found")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
