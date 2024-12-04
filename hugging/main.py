# extraido de https://huggingface.co/docs/api-inference/getting-started
# https://huggingface.co/models?inference=warm&sort=trending
import requests
from create_env import TOKEN
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
#API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": f"Bearer {TOKEN}"}

data = {
    "inputs": "Erase una vez",
    "parameters": {
        "max_new_tokens": 600,
        "temperature": 0.1,    # Controla la creatividad (0.7 = razonable)
        "top_p": 0.9,         # Limita las palabras a las más probables
        "repetition_penalty": 1.2  # Penaliza repeticiones de palabras/frases
    }
}

response = requests.post(API_URL, headers=headers, json=data)
print(response.json())
