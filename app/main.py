from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "AI backend running"}
# uvicorn app.main:app --reload