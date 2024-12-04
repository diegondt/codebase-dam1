import requests
from create_env import TOKEN

API_URL = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
headers = {"Authorization": f"Bearer {TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": "Que buen dia hace",
})

emociones = output[0]

for emocion in emociones:
	print(emocion['label'] + ":", emocion['score'])
	print(emocion.get('label') + ":", emocion.get('score'))
