"""FastAPI API exposing /calculate endpoint for concatenated binary problem."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .core import concatenated_binary

app = FastAPI(title="Concatenated Binary API", version="1.0.0")


class CalcRequest(BaseModel):
    n: int


class CalcResponse(BaseModel):
    n: int
    result: int


@app.post("/calculate", response_model=CalcResponse)
def calculate(req: CalcRequest):
    if req.n < 1:
        raise HTTPException(status_code=400, detail="n must be >= 1")
    value = concatenated_binary(req.n)
    return CalcResponse(n=req.n, result=value)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
