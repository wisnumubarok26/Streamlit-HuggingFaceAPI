import requests

API_URL = "https://api-inference.huggingface.co/models/StevenLimcorn/indonesian-roberta-base-emotion-classifier"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()




