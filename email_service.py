import time
import logging
import os
import pandas as pd

from datetime import datetime

# Create folders automatically
os.makedirs("app/logs", exist_ok=True)
os.makedirs("app/reports", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="app/logs/email.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

# DRY RUN MODE
# True = simulate emails
# False = real email sending later
DRY_RUN = True


# Save reports to CSV
def save_report(name, email, reminder_type, status):

    report_data = pd.DataFrame([{
        "timestamp": datetime.now(),
        "name": name,
        "email": email,
        "reminder_type": reminder_type,
        "status": status
    }])

    report_path = "app/reports/email_report.csv"

    # Append data if report already exists
    if os.path.exists(report_path):

        report_data.to_csv(
            report_path,
            mode="a",
            header=False,
            index=False
        )

    else:

        report_data.to_csv(
            report_path,
            index=False
        )


# Email sending function
def send_email(name, email, reminder_type, reminder_date):

    print("\nPreparing Email...")
    time.sleep(1)

    subject = f"{reminder_type} Reminder"

    message = f"""
Hello {name},

This is a reminder regarding your upcoming {reminder_type}.

Scheduled Date: {reminder_date}

Thank You,
Automation Team
"""

    try:

        if DRY_RUN:

            output = f"""
====================================
DRY RUN MODE - EMAIL SIMULATION
====================================

To: {email}
Subject: {subject}

Message:
{message}

Status: SIMULATED SUCCESS
====================================
            """

            print(output)

            # Save logs
            logging.info(
                f"SIMULATED EMAIL SENT TO {email} | Reminder: {reminder_type}"
            )

            # Save CSV report
            save_report(
                name,
                email,
                reminder_type,
                "SUCCESS"
            )

            # Flush logs immediately
            for handler in logging.getLogger().handlers:
                handler.flush()

        else:
            print("Real Email Sending Enabled")

    except Exception as e:

        print(f"Error: {e}")

        logging.error(
            f"FAILED EMAIL TO {email} | ERROR: {e}"
        )

        # Save failed report
        save_report(
            name,
            email,
            reminder_type,
            "FAILED"
        )

        for handler in logging.getLogger().handlers:
            handler.flush()