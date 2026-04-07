import time
from datetime import datetime
from firebase_db import get_reminders

def run_scheduler():

    print("⏳ Scheduler started...")

    while True:
        reminders = get_reminders("user1")

        now = datetime.now()

        for r in reminders:
            try:
                reminder_time = datetime.fromisoformat(r["time"])

                if r["status"] == "pending" and reminder_time <= now:
                    print(f"🔔 REMINDER: {r['task']}")

            except Exception as e:
                print("Error:", e)

        time.sleep(10)  # check every 10 sec