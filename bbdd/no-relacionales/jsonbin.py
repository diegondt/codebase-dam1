import dotenv
import os
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("API_KEY")
BIN_ID = os.getenv("BIN_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")

def get_json():
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "X-Master-Key": API_KEY,
        "X-Access-Key": ACCESS_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

def update_json(data):
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "X-Master-Key": API_KEY,
        "X-Access-Key": ACCESS_KEY,
        "Content-Type": "application/json",
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

def delete_json():
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "X-Master-Key": API_KEY,
        "X-Access-Key": ACCESS_KEY
    }
    response = requests.delete(url, headers=headers)
    return response.json()

def patch_json(data):
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "X-Master-Key": API_KEY,
        "X-Access-Key": ACCESS_KEY,
        "Content-Type": "application/json",
    }
    response = requests.patch(url, headers=headers, json=data)
    return response.json()
print(get_json())
update_json({"username": "admin", "password": "admin"})
patch_json({"username": "user0", "password": "user0"})
print(get_json())
