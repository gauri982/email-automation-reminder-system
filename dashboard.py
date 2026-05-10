import streamlit as st
import pandas as pd

# Page title
st.set_page_config(
    page_title="Email Automation Dashboard",
    layout="wide"
)

st.title("📧 Email Automation & Reminder Dashboard")

# Load data
contacts = pd.read_csv("data/contacts.csv")
reminders = pd.read_csv("data/reminders.csv")
reports = pd.read_csv("app/reports/email_report.csv")

# Metrics
total_contacts = len(contacts)
total_reminders = len(reminders)
total_reports = len(reports)

success_count = len(
    reports[reports["status"] == "SUCCESS"]
)

failed_count = len(
    reports[reports["status"] == "FAILED"]
)

# Dashboard metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Contacts", total_contacts)
col2.metric("Reminders", total_reminders)
col3.metric("Reports", total_reports)
col4.metric("Success", success_count)
col5.metric("Failed", failed_count)

st.divider()

# Contacts table
st.subheader("📋 Contacts")

st.dataframe(
    contacts,
    use_container_width=True
)

# Reminder table
st.subheader("⏰ Reminders")

st.dataframe(
    reminders,
    use_container_width=True
)

# Reports table
st.subheader("📊 Email Reports")

st.dataframe(
    reports,
    use_container_width=True
)

# Status chart
st.subheader("📈 Email Status Summary")

status_data = reports["status"].value_counts()

st.bar_chart(status_data)