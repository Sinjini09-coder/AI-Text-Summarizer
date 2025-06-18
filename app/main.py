from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from app.summarizer import generate_summary

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/")
async def summarize(text: str = Form(...)):
    summary = generate_summary(text)
    return {"summary": summary}