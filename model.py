from dotenv import load_dotenv
import os
import requests

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mengakses variabel lingkungan API
API = os.getenv('API')

API_URL = "https://api-inference.huggingface.co/models/StevenLimcorn/indonesian-roberta-base-emotion-classifier"
headers = {"Authorization": f"Bearer {API}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

