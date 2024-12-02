import requests
import dotenv
import os
dotenv.load_dotenv()

API_KEY = os.getenv("API_KEY")
BIN_ID = os.getenv("BIN_ID")
ACCESS_KEY = os.getenv("ACCESS_KEY")

url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
headers = {
    'Content-Type': 'application/json',
    "X-Master-Key": API_KEY,
    "X-Access-Key": ACCESS_KEY
}

def read_db():
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print("read_db", data)
    return data.get("record", {})

def update_db(obj):
    response = requests.put(url, headers=headers, json=obj)
    data = response.json()
    print("update_db", data)
    return data.get("record")

def get_users():
    return read_db().get("users", [])


def add_user(user, password):
    db = get_users()
    db.append({"user": user, "password": password})
    return update_db({"users": db})

db = {
    "users": []
}

db["users"].append({"user": "admin", "password": "admin"})
db["users"].append({"user": "mod", "password": "mod"})

update_db(db)
add_user("usuario0", "usuario0")
users = get_users()
for user in users:
    print(user.get("user"),":", user.get("password"))