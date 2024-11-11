
from routes import login, smc, dwt
from fastapi import FastAPI, File


app = FastAPI(
    title="Fall 2024 scince work N.V Zadiran",
    description="""Fullstack Fastapi Postgress Streamlit app for ores experimental data  Higland Gold
    """,
    version="0.1.0",
)


app.include_router(login.router, prefix="/api/login")

app.include_router(smc.router, prefix="/api/smc")
app.include_router(dwt.router,  prefix="/api/dwt")

@app.get("/api/health_check")
async def health_check():
    return {"status": "success"}

