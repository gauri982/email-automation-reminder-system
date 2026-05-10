from fastapi import FastAPI
import pandas as pd

app = FastAPI(
    title="Email Automation & Reminder System",
    description="Automation Backend APIs",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Email Automation System Running"
    }


# Get all contacts
@app.get("/contacts")
def get_contacts():

    contacts = pd.read_csv("data/contacts.csv")

    return contacts.to_dict(orient="records")


# Get all reminders
@app.get("/reminders")
def get_reminders():

    reminders = pd.read_csv("data/reminders.csv")

    return reminders.to_dict(orient="records")


# Get generated reports
@app.get("/reports")
def get_reports():

    reports = pd.read_csv(
        "app/reports/email_report.csv"
    )

    return reports.to_dict(orient="records")