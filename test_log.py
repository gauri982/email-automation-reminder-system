import logging
import os

# Create folder if missing
os.makedirs("app/logs", exist_ok=True)

# Configure logger
logging.basicConfig(
    filename="app/logs/email.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Writing log...")

logging.info("TEST LOG ENTRY")

print("Done")