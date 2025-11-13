# Job Application Tracker API

A RESTful API built with FastAPI and Supabase for managing job applications, CVs, user profiles, and related data.

## Features

- Full CRUD operations for all tables
- RESTful API endpoints
- Supabase database integration
- Automatic API documentation
- CORS support

## Project Structure

```
python-test-api/
├── routers/
│   ├── __init__.py
│   ├── profiles.py
│   ├── cvs.py
│   ├── jobs.py
│   ├── job_applications.py
│   ├── application_timeline.py
│   ├── user_settings.py
│   └── saved_searches.py
├── main.py
├── models.py
├── database.py
├── config.py
├── requirements.txt
└── .env
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. The `.env` file is already configured with your Supabase credentials.

3. Run the application:
```bash
python main.py
```

Or with uvicorn:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available Endpoints

### Profiles
- `GET /profiles/` - Get all profiles
- `GET /profiles/{profile_id}` - Get a specific profile
- `POST /profiles/` - Create a new profile
- `PUT /profiles/{profile_id}` - Update a profile
- `DELETE /profiles/{profile_id}` - Delete a profile

### CVs
- `GET /cvs/` - Get all CVs (supports `?user_id=` filter)
- `GET /cvs/{cv_id}` - Get a specific CV
- `POST /cvs/` - Create a new CV
- `PUT /cvs/{cv_id}` - Update a CV
- `DELETE /cvs/{cv_id}` - Delete a CV

### Jobs
- `GET /jobs/` - Get all jobs (supports filters: `user_id`, `company`, `location`, `job_type`, `is_remote`, `status`)
- `GET /jobs/{job_id}` - Get a specific job
- `POST /jobs/` - Create a new job
- `PUT /jobs/{job_id}` - Update a job
- `DELETE /jobs/{job_id}` - Delete a job

### Job Applications
- `GET /job-applications/` - Get all applications (supports filters: `user_id`, `job_id`, `status`)
- `GET /job-applications/{application_id}` - Get a specific application
- `POST /job-applications/` - Create a new application
- `PUT /job-applications/{application_id}` - Update an application
- `DELETE /job-applications/{application_id}` - Delete an application

### Application Timeline
- `GET /application-timeline/` - Get all timeline events (supports filters: `application_id`, `event_type`)
- `GET /application-timeline/{event_id}` - Get a specific event
- `POST /application-timeline/` - Create a new event
- `PUT /application-timeline/{event_id}` - Update an event
- `DELETE /application-timeline/{event_id}` - Delete an event

### User Settings
- `GET /user-settings/` - Get all user settings
- `GET /user-settings/{user_id}` - Get settings for a specific user
- `POST /user-settings/` - Create user settings
- `PUT /user-settings/{user_id}` - Update user settings
- `DELETE /user-settings/{user_id}` - Delete user settings

### Saved Searches
- `GET /saved-searches/` - Get all saved searches (supports `?user_id=` filter)
- `GET /saved-searches/{search_id}` - Get a specific saved search
- `POST /saved-searches/` - Create a new saved search
- `PUT /saved-searches/{search_id}` - Update a saved search
- `DELETE /saved-searches/{search_id}` - Delete a saved search

## Example API Usage

### Create a Profile
```bash
curl -X POST "http://localhost:8000/profiles/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "full_name": "John Doe",
    "subscription_tier": "premium"
  }'
```

### Get All Jobs with Filters
```bash
curl "http://localhost:8000/jobs/?is_remote=true&job_type=full-time"
```

### Create a Job Application
```bash
curl -X POST "http://localhost:8000/job-applications/" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user-uuid",
    "job_id": "job-uuid",
    "cv_id": "cv-uuid",
    "status": "applied"
  }'
```

## Database Schema

The API supports the following tables:
- **profiles** - User profile information
- **cvs** - CV/Resume data with skills, experience, and education
- **jobs** - Job listings and opportunities
- **job_applications** - Applications submitted by users
- **application_timeline** - Timeline of events for each application
- **user_settings** - User preferences and notification settings
- **saved_searches** - Saved job search parameters

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **Supabase** - Backend as a Service with PostgreSQL database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server for running the application
