from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "todo service is running"}
