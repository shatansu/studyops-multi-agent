import time
from datetime import datetime, timezone
from firebase_db import get_reminders

def run_scheduler():

    print("⏳ Scheduler started...")

    while True:
        reminders = get_reminders("user1")

        now = datetime.now(timezone.utc)

        for r in reminders:
            try:
                reminder_time = datetime.fromisoformat(r["time"])

                # fix timezone
                if reminder_time.tzinfo is None:
                    reminder_time = reminder_time.replace(tzinfo=timezone.utc)

                if r["status"] == "pending" and reminder_time <= now:
                    print(f"🔔 REMINDER: {r['task']}")

            except Exception as e:
                print("Error:", e)

        time.sleep(10)