from firebase_db import save_task, save_notes
from firebase_db import save_reminder

def create_task(task):
    save_task(task)
    return {"status": "task_saved"}

def store_notes(notes):
    save_notes(notes)
    return {"status": "notes_saved"}

    

def create_reminder(reminder):
    save_reminder(reminder)
    return {"status": "reminder_saved"}