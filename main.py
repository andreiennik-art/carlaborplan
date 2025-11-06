from estimates import router as estimates_router
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Carlabor Estimator")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/")
def index():
    return {"status": "Carlabor backend works!"}

# ✅ подключаем расчёты
app.include_router(estimates_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

