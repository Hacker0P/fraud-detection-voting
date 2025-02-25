import streamlit as st
import requests

# Corrected API URL
API_URL = "https://fraud-detection-voting.onrender.com/submit_vote/"

st.title("🗳️ Fraud Detection Voting System")

# Input fields
voter_id = st.text_input("Voter ID")
candidate = st.text_input("Candidate Name")
location = st.text_input("Location")
biometric_hash = st.text_input("Biometric Hash")
timestamp = st.text_input("Timestamp (YYYY-MM-DDTHH:MM:SSZ)", "2025-02-25T12:00:00Z")

if st.button("Submit Vote"):
    data = {
        "voter_id": voter_id,
        "candidate": candidate,
        "location": location,
        "biometric_hash": biometric_hash,
        "timestamp": timestamp
    }
    
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        st.success("✅ Vote submitted successfully!")
    else:
        st.error("❌ Error: " + response.text)
