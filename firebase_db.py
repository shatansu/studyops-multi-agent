import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# 🔹 SAVE TASK
def save_task(task):
    task["created_at"] = datetime.now().isoformat()
    db.collection("tasks").add(task)

# 🔹 SAVE NOTES
def save_notes(notes):
    notes["created_at"] = datetime.now().isoformat()
    db.collection("notes").add(notes)

# 🔹 GET TASKS
def get_tasks(user_id):
    docs = db.collection("tasks").where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]

# 🔹 GET NOTES
def get_notes(user_id):
    docs = db.collection("notes").where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]

    # 🔹 SAVE REMINDER
def save_reminder(reminder):
    reminder["created_at"] = datetime.now().isoformat()
    db.collection("reminders").add(reminder)

# 🔹 GET REMINDERS
def get_reminders(user_id):
    docs = db.collection("reminders").where("user_id", "==", user_id).stream()
    return [doc.to_dict() for doc in docs]