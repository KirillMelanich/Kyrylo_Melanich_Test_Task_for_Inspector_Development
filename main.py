from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

DJANGO_API_URL = "http://127.0.0.1:8000/api/"


@app.post("/create_user_pool/")
async def create_user_pool(payload: dict):
    try:
        response = requests.post(f"{DJANGO_API_URL}staking_app/staking_pool/", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error in making request to Django service: {e}")
