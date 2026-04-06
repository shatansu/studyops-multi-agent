from firebase_db import save_task, save_notes

def create_task(task):
    save_task(task)
    return {"status": "task_saved"}

def store_notes(notes):
    save_notes(notes)
    return {"status": "notes_saved"}