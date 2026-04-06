import firebase_admin
from firebase_admin import credentials, firestore

# initialize
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


# 🔹 Save task
def save_task(task):
    db.collection("tasks").add(task)


# 🔹 Save notes
def save_notes(notes):
    db.collection("notes").add(notes)