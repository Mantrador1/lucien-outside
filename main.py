from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class CommandRequest(BaseModel):
    command: str

@app.get("/")
async def root():
    return {"message": "Lucien Proxy Online"}

@app.post("/command")
async def command_endpoint(request: CommandRequest):
    if request.command == "ping":
        return {"response": "pong"}
    return {"response": f"Unknown command: {request.command}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

