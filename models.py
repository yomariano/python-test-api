from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime


# Profile Models
class ProfileBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    subscription_tier: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# CV Models
class CVBase(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    file_name: Optional[str] = None
    file_url: Optional[str] = None
    content: Optional[str] = None
    skills: Optional[List[str]] = None
    experience: Optional[List[Dict[str, Any]]] = None
    education: Optional[List[Dict[str, Any]]] = None
    is_primary: Optional[bool] = False


class CVCreate(CVBase):
    user_id: str


class CVUpdate(CVBase):
    pass


class CV(CVBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Job Models
class JobBase(BaseModel):
    user_id: Optional[str] = None
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None
    is_remote: Optional[bool] = False
    site: Optional[str] = None
    job_url: Optional[str] = None
    description: Optional[str] = None
    date_posted: Optional[datetime] = None
    date_scraped: Optional[datetime] = None
    status: Optional[str] = None


class JobCreate(JobBase):
    pass


class JobUpdate(JobBase):
    pass


class Job(JobBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Job Application Models
class JobApplicationBase(BaseModel):
    user_id: Optional[str] = None
    job_id: Optional[str] = None
    cv_id: Optional[str] = None
    tailored_cv_content: Optional[str] = None
    cover_letter: Optional[str] = None
    status: Optional[str] = None
    ai_match_score: Optional[int] = None
    ai_improvements: Optional[List[Dict[str, Any]]] = None
    applied_at: Optional[datetime] = None


class JobApplicationCreate(JobApplicationBase):
    user_id: str
    job_id: str


class JobApplicationUpdate(JobApplicationBase):
    pass


class JobApplication(JobApplicationBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Application Timeline Models
class ApplicationTimelineBase(BaseModel):
    application_id: Optional[str] = None
    event_type: Optional[str] = None
    event_description: Optional[str] = None
    event_data: Optional[Dict[str, Any]] = None


class ApplicationTimelineCreate(ApplicationTimelineBase):
    application_id: str


class ApplicationTimelineUpdate(ApplicationTimelineBase):
    pass


class ApplicationTimeline(ApplicationTimelineBase):
    id: str
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# User Settings Models
class UserSettingsBase(BaseModel):
    email_notifications: Optional[bool] = True
    job_alerts: Optional[bool] = True
    preferred_locations: Optional[List[str]] = None
    preferred_job_types: Optional[List[str]] = None
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    remote_only: Optional[bool] = False
    settings_data: Optional[Dict[str, Any]] = None


class UserSettingsCreate(UserSettingsBase):
    user_id: str


class UserSettingsUpdate(UserSettingsBase):
    pass


class UserSettings(UserSettingsBase):
    user_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Saved Search Models
class SavedSearchBase(BaseModel):
    user_id: Optional[str] = None
    search_name: Optional[str] = None
    search_params: Optional[Dict[str, Any]] = None
    notification_enabled: Optional[bool] = False


class SavedSearchCreate(SavedSearchBase):
    user_id: str


class SavedSearchUpdate(SavedSearchBase):
    pass


class SavedSearch(SavedSearchBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
