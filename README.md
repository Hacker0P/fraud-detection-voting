# Fraud Detection in Voting

This project is a full-stack application that detects fraudulent voting activities using **machine learning** and **biometric verification**. The system consists of a **frontend (Streamlit)** and a **backend (FastAPI)** with a **SQLite database** for secure and efficient fraud detection.

## Live Demo

- **Frontend (Streamlit UI):** ![Frontend](https://raw.githubusercontent.com/Hacker0P/fraud-detection-voting/main/frontend.jpg)
- **Backend (FastAPI API):** ![Backend](https://raw.githubusercontent.com/Hacker0P/fraud-detection-voting/main/backend.jpg)

## Available Scripts

### `npm start`

Runs the FastAPI backend in development mode.  
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to access the API locally.

### `streamlit run app.py`

Runs the Streamlit frontend in development mode.  
It opens automatically in your default web browser.

### `pip install -r requirements.txt`

Installs all necessary dependencies for both frontend and backend.  
Ensure you run this command in both `src/frontend` and `src/backend` directories before starting the project.

### `uvicorn main:app --reload`

Starts the FastAPI backend server with live reloading.  
Use this when developing and testing API endpoints.

## Features

- ✅ Secure vote submission with biometric authentication.  
- ✅ Fraud detection using machine learning models.  
- ✅ Interactive UI built with Streamlit.  
- ✅ FastAPI-based backend for handling vote data.  
- ✅ SQLite database for storing votes.  
- ✅ CORS support for frontend-backend communication.  

## Technologies Used

### Frontend
- **Streamlit** (for UI)
- **Requests** (for API communication)

### Backend
- **FastAPI** (for API development)
- **SQLite** (for database storage)
- **SQLAlchemy** (ORM for database interactions)
- **Pydantic** (for data validation)
- **CORS Middleware** (for cross-origin access)

## How It Works

1. **Users enter vote details (Voter ID, Candidate, Location, Biometric Hash, Timestamp)** in the Streamlit frontend.
2. **Frontend sends the vote data to the FastAPI backend**, which processes and stores it in the SQLite database.
3. **Fraud detection algorithms analyze voting patterns** and flag suspicious activities.
4. **Results are displayed in the frontend** for easy visualization.

## Screenshots

### Frontend (Streamlit UI)
![Frontend](img src="https://raw.githubusercontent.com/Hacker0P/fraud-detection-voting/frontend.jpg" width="100%")

### Backend (FastAPI with Database)
![Backend](img src="https://raw.githubusercontent.com/Hacker0P/fraud-detection-voting/main/backend.jpg" width="100%")

## Deployment

The project is deployed using:  
- **Frontend:** Streamlit Cloud 
- **Backend:** Render 

#### Steps to Deploy

1. **Frontend Deployment:**
   - Push frontend code to GitHub.
   - Deploy using Streamlit Sharing.
   - Update the API URL in the frontend code.

2. **Backend Deployment:**
   - Push backend code to GitHub.
   - Deploy using Render.
   - Set up the database and API endpoints.

## Future Enhancements

- 🔹 Real-time fraud detection.  
- 🔹 Advanced ML models (BERT, RoBERTa, etc.).  
- 🔹 Blockchain-based secure voting.  
- 🔹 Cloud-based authentication & storage.  

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, reach out via [shibamkundu120103@gmail.com] or open an issue in the repository.
