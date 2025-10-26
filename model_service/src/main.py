from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/health")
def health():
    return PlainTextResponse("HEALTH-OK")

@app.get("/ready")
def ready():
    return PlainTextResponse("READY-OK")

@app.post("/infer")
def infer(req: Request):
    return {"message": "inference executed", "status": "done"}
