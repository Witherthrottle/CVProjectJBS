from fastapi import FastAPI

app = FastAPI(title="Inspection API", version="1.0")

@app.get("/")
async def root():
    return {"message": "API is running!"}