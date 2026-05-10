import pandas as pd

from apscheduler.schedulers.blocking import BlockingScheduler

from email_service import send_email

# Load CSV files
contacts = pd.read_csv("data/contacts.csv")
reminders = pd.read_csv("data/reminders.csv")

scheduler = BlockingScheduler()


def reminder_job():

    print("\nChecking reminders...\n")

    for _, reminder in reminders.iterrows():

        # Match contact with reminder
        matched_contact = contacts[
            contacts["id"] == reminder["contact_id"]
        ]

        if not matched_contact.empty:

            contact = matched_contact.iloc[0]

            print(f"Processing: {contact['name']}")

            # Call email service
            send_email(
                contact["name"],
                contact["email"],
                reminder["reminder_type"],
                reminder["reminder_date"]
            )

        else:
            print("No matching contact found")


# Run every 30 seconds
scheduler.add_job(
    reminder_job,
    trigger="interval",
    seconds=30
)

print("Scheduler Started...")

# Run once immediately
reminder_job()

# Start scheduler
scheduler.start()