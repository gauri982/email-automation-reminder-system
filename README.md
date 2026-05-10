# 📧 Email Automation & Reminder System

## 🚀 Project Overview

The Email Automation & Reminder System is a Python-based automation tool designed to send scheduled and personalized emails using SMTP. It helps automate repetitive communication tasks such as reminders, notifications, follow-ups, and alerts using CSV-based input data.

This project simulates real-world business email automation systems used in HR, operations, marketing, and productivity workflows.

---

## 🎯 Problem Statement

In many organizations, sending repetitive emails manually leads to:
- ⏳ Time wastage  
- ❌ Human errors  
- 📉 Poor tracking of communication  
- 🔁 Repetitive workload  

This system solves these issues by automating:
- Email scheduling  
- Personalized messaging  
- Reminder generation  
- Delivery tracking  

---

## 💡 Features

- 📩 Automated email sending using SMTP  
- 📅 Scheduled reminders (daily/weekly/custom)  
- 📊 CSV-based contact management  
- ✉️ Personalized email messages  
- 🧾 Logging system (success/failure tracking)  
- 📁 Report generation  
- 🧪 Safe execution (dry-run support)  
- 🔐 Secure credentials using environment variables  

---

## 🏗️ Tech Stack

- Python 🐍  
- smtplib  
- email.message  
- Pandas  
- CSV handling  
- datetime  
- logging  
- python-dotenv  

---

## 📁 Project Structure


Email-Automation-Reminder-System/
│
├── data/ # CSV input files (contacts, reminders)
├── templates/ # Email templates
├── src/ # Core logic (email sender, scheduler)
├── outputs/ # Generated reports
├── logs/ # Success and error logs
├── images/ # Screenshots
├── docs/ # Documentation
├── main.py # Entry point
├── requirements.txt # Dependencies
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/gauri982/email-automation-reminder-system.git
cd email-automation-reminder-system
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Environment Variables

Create a .env file:

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

⚠️ Never upload .env to GitHub

▶️ How to Run
Run normally:
python main.py
Run in safe mode (no email sent):
python main.py --dry-run
📊 Workflow
CSV Contacts → Load Data → Personalize Email → Schedule Reminder → Send Email → Logging → Report Generation
📁 Sample CSV Format
contacts.csv
name,email,role
John Doe,john@example.com,HR
Sara Khan,sara@example.com,Manager
🧾 Output Generated
Sent emails log
Failed emails log
Execution logs
CSV reports
🖼️ Screenshots

Below is the output of the Email Automation & Reminder System dashboard:

📌 Dashboard Output

This shows the system interface and automation results.

🎯 Learning Outcomes

This project demonstrates:

Email automation using Python
Task scheduling concepts
File handling (CSV)
Real-world backend workflows
Logging and debugging systems
Automation system design
💼 Industry Use Cases
HR reminder systems
CRM email automation
Marketing campaigns
Webinar reminders
Task notification systems
⚠️ Important Notes
Do NOT upload .env file
Do NOT upload venv/ folder
Use dry-run mode for testing
Use Gmail App Password instead of normal password
👨‍💻 Author
gauri k
Developed as a student project to demonstrate Python automation, scheduling, and real-world backend system design for GitHub portfolio and internships.

🚀 Future Improvements
FastAPI backend integration
Streamlit dashboard UI
Email analytics dashboard
Database support (SQLite/PostgreSQL)
Cloud deployment (Render/Railway)