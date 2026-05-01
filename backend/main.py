import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# --- DYNAMIC PATH SETTINGS ---
# Finds the 'frontend' folder relative to this 'backend' folder
current_script_dir = os.path.dirname(os.path.abspath(__file__))
base_project_path = os.path.dirname(current_script_dir)
frontend_path = os.path.join(base_project_path, "frontend")

TEMPLATES_DIR = os.path.join(frontend_path, "templates")
STATIC_DIR = os.path.join(frontend_path, "static")

# Initialize templates and mount static files
templates = Jinja2Templates(directory=TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

class SymptomData(BaseModel):
    symptoms: str
    age: int = None

# --- PAGE ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def read_landing(request: Request):
    return templates.TemplateResponse(request, "landing.html")

@app.get("/result", response_class=HTMLResponse)
async def read_result(request: Request):
    return templates.TemplateResponse(request, "result.html")

# --- AI ANALYSIS API ---

@app.post("/api/analyze")
async def analyze_symptoms(data: SymptomData):
    symptoms_lower = data.symptoms.lower()
    
    # Logic for Specialist, Severity, and Reasoning
    if any(word in symptoms_lower for word in ["chest pain", "heart", "breathless", "bp"]):
        specialist = "Cardiologist"
        severity = "High - Emergency"
        reasoning = "Symptoms indicate potential cardiovascular distress. Immediate consultation is required."
        docs = [
            {"name": "Dr. Atul (Senior Cardiologist)", "fee": "₹1500", "wait": "Immediate"},
            {"name": "Dr. Anshika (Cardiology Specialist)", "fee": "₹1200", "wait": "10 mins"}
        ]
    elif any(word in symptoms_lower for word in ["headache", "migraine", "brain", "dizzy"]):
        specialist = "Neurologist"
        severity = "Moderate"
        reasoning = "Neurological symptoms detected. A specialist review is advised to rule out chronic issues."
        docs = [
            {"name": "Dr. Anshika (Neurology)", "fee": "₹1000", "wait": "15 mins"},
            {"name": "Dr. Atul (Neuro-Consultant)", "fee": "₹1300", "wait": "20 mins"}
        ]
    else:
        specialist = "General Physician"
        severity = "Standard"
        reasoning = "General symptoms reported. A routine check-up with a physician is recommended."
        docs = [
            {"name": "Dr. Anshika", "fee": "₹5000", "wait": "5 mins"},
            {"name": "Dr. Atul", "fee": "₹5500", "wait": "10 mins"}
        ]

    return {
        "specialist": specialist,
        "severity": severity,
        "reasoning": reasoning,
        "doctors_nearby": docs
    }