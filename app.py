from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from llm_utils import get_symptom_analysis
from database import save_query
from schemas import SymptomInput, SymptomOutput

app = FastAPI()

# Serve index.html from root folder
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/check", response_model=SymptomOutput)
async def check_symptoms(symptom: SymptomInput):
    result = get_symptom_analysis(symptom.text)
    save_query(symptom.text, result)
    return result
