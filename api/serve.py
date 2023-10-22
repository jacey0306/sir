from fastapi import FastAPI
import json
from fastapi.responses import RedirectResponse
import main as sir
from .models import SIRRequest

app = FastAPI(version="0.0.0",
              title="SIR.PY",
              description="A simple python sir modeler.")

@app.get("/")
async def root():
    return RedirectResponse(url='docs')

@app.post('/count_infected')
async def post_count_infected(req: SIRRequest):
    count_infected = sir.count_infected(req.city)
    results = {"count_infected": count_infected}

    return results


