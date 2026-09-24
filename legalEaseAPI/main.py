from fastapi import FastAPI
import uvicorn
from legalEaseAPI.routes import router

app = FastAPI(title="LegalEase - AI Legal Document Generator")

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to LegalEase AI Legal Document Generator API"}

if __name__ == "__main__":
    uvicorn.run("legalEaseAPI.main:app", host="0.0.0.0", port=8000, reload=True)
