# TriNova Health — Smart Symptom Analyzer

> Team: **TriNova** | Leader: **Arpita Raj** | Track: **Health Tech** | Hackathon 2026

---

## Project Overview

TriNova is an AI-powered pre-consultation health tool that helps patients identify
the right medical specialist for their symptoms before booking an appointment.

**Core Features:**
- Symptom input (text + quick-select chips)
- AI-powered specialist recommendation (Gemini AI + rule-based fallback)
- Severity detection: Low / Medium / High
- Emergency alert system
- Personalized recommendations based on age & gender
- 13 specialist categories covered

---

## Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Frontend  | HTML5, CSS3, Vanilla JavaScript     |
| Backend   | Python 3.11+, FastAPI               |
| AI Engine | Google Gemini 1.5 Flash API         |
| Fallback  | Rule-based symptom matching (JSON)  |
| Server    | Uvicorn (ASGI)                      |

---

## Project Structure

```
trinova/
├── backend/
│   ├── main.py              ← FastAPI app (routes, AI logic)
│   ├── symptom_data.json    ← Specialist mappings & rules
│   ├── requirements.txt     ← Python dependencies
│   └── .env.example         ← Environment variable template
│
└── frontend/
    ├── templates/
    │   └── index.html       ← Main HTML page
    └── static/
        ├── css/style.css    ← Stylesheet
        └── js/app.js        ← Frontend logic
```

---

## Setup Instructions

### 1. Clone / Download the project

```bash
cd trinova/backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and add your **Gemini API Key**:

```
GEMINI_API_KEY=your_actual_key_here
```

Get your free Gemini API key at: https://aistudio.google.com/app/apikey

> **No API key?** The app still works using the built-in rule-based engine.

### 5. Run the server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Open in browser

```
http://localhost:8000
```

---

## API Endpoints

| Method | Endpoint          | Description                         |
|--------|-------------------|-------------------------------------|
| GET    | `/`               | Serves the main web app             |
| POST   | `/api/analyze`    | Analyze symptoms → returns result   |
| GET    | `/api/specialists`| List all supported specialists      |
| GET    | `/api/health`     | Health check + config status        |

### POST `/api/analyze` — Request body

```json
{
  "symptoms": "severe headache, fever, neck stiffness for 3 days",
  "age": 28,
  "gender": "female"
}
```

### Response

```json
{
  "specialist": "Neurologist",
  "specialist_description": "...",
  "severity": "high",
  "emergency": false,
  "emergency_message": "",
  "reasoning": "...",
  "recommendations": ["...", "..."],
  "confidence": "ai_enhanced",
  "disclaimer": "..."
}
```

---

## How AI Logic Works

```
User input
    │
    ▼
Emergency keyword scan (rule-based, always runs)
    │
    ├─ GEMINI_API_KEY set? ──→ YES ──→ Gemini 1.5 Flash API call
    │                                         │
    │                          JSON parsed → merged with rule-based
    │
    └─ NO ──→ Rule-based engine
                  │
                  ├─ Severity detection (keyword weights)
                  ├─ Specialist matching (symptom overlap score)
                  └─ Recommendation builder
```

---

## Future Scope

- Integration with real hospital booking systems
- Machine learning model trained on symptom datasets
- Real-time doctor availability tracking
- Location-based emergency service routing
- Multi-language support

---

## Disclaimer

TriNova is a decision-support tool only. It does **not** replace professional
medical diagnosis. For emergencies, call **112** immediately.

---

*Built with ❤️ by Team TriNova for the 2026 Health Tech Hackathon*