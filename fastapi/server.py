from routes import login, smc
from fastapi import FastAPI, File


app = FastAPI(
    title="Fall 2024 scince work N.V Zadiran",
    description="""Fullstack Fastapi Postgress Streamlit app for ores experimental data  Higland Gold
    """,
    version="0.1.0",
)


app.include_router(login.router, prefix="/login")


app.include_router(smc.router, prefix="/smc")
@app.get("/health_check")
async def health_check():
    return {"status": "success"}

