import requests

# Corrected API URL
API_URL = "https://fraud-detection-voting.onrender.com/submit_vote/"

data = {
    "voter_id": "12345",
    "candidate": "John Doe",
    "location": "New York",
    "biometric_hash": "abc123xyz",
    "timestamp": "2025-02-25T12:00:00Z"
}

response = requests.post(API_URL, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
