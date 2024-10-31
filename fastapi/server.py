from routes import login
from fastapi import FastAPI, File


app = FastAPI(
    title="Fall 2024 scince work N.V Zadiram",
    description="""Fullstack Fastapi Postgress Streamlit app for ores experimental data  Higland Gold
    """,
    version="0.1.0",
)


app.include_router(login.router, prefix="/login")


@app.get("/health_check")
async def health_check():
    return {"status": "success"}

