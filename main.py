from fastapi import FastAPI
from app.routes import router  # Import the router from routes.py

app = FastAPI()

# Include the router so FastAPI knows about the routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Task Management API is running!"}
