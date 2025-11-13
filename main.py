from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    profiles,
    cvs,
    jobs,
    job_applications,
    application_timeline,
    user_settings,
    saved_searches,
)

# Create FastAPI app
app = FastAPI(
    title="Job Application Tracker API",
    description="RESTful API for managing job applications, CVs, and user profiles",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://shapemycv.xyz",
        "http://localhost:3000",  # For local development
        "http://localhost:5173",  # For Vite dev server
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profiles.router)
app.include_router(cvs.router)
app.include_router(jobs.router)
app.include_router(job_applications.router)
app.include_router(application_timeline.router)
app.include_router(user_settings.router)
app.include_router(saved_searches.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Job Application Tracker API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
