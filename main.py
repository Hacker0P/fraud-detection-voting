from fastapi import FastAPI, Depends, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # CORS Fix
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all frontend domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Database setup
DATABASE_URL = "sqlite:///./votes.db"  # SQLite Database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# WebSocket connections
connected_clients = []

# Vote Model for Database
class Vote(Base):
    __tablename__ = "votes"
    
    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(String, unique=True, index=True)  # Unique voter ID
    candidate = Column(String, index=True)
    location = Column(String)
    timestamp = Column(DateTime)
    biometric_hash = Column(String, unique=True)  # Prevent duplicate biometric votes

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Model for API Requests
class VoteRequest(BaseModel):
    voter_id: str
    candidate: str
    location: str
    timestamp: str
    biometric_hash: str

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Fraud Detection Voting API is Running!"}

# Fraud Detection Function
def detect_fraud(vote: VoteRequest, db: Session):
    vote_time = datetime.strptime(vote.timestamp, "%Y-%m-%dT%H:%M:%SZ")

    existing_votes = db.query(Vote).all()
    for v in existing_votes:
        # Prevent duplicate voter ID
        if v.voter_id == vote.voter_id:
            return "Fraud detected: Duplicate voter ID!"

        # Prevent multiple votes using the same biometric hash
        if v.biometric_hash == vote.biometric_hash:
            return "Fraud detected: Same biometric data used for multiple voters!"

        # Detect rapid voting from the same location (within 5 minutes)
        if v.location == vote.location and abs((vote_time - v.timestamp.replace(tzinfo=None)).total_seconds()) < 300:
            return "Fraud detected: Too many votes from the same location in a short time!"

    return None  # No fraud detected

# Submit a Vote
@app.post("/submit_vote/")
async def submit_vote(vote: VoteRequest, db: Session = Depends(get_db)):
    fraud_message = detect_fraud(vote, db)

    if fraud_message:
        raise HTTPException(status_code=400, detail=fraud_message)

    new_vote = Vote(
        voter_id=vote.voter_id,
        candidate=vote.candidate,
        location=vote.location,
        timestamp=datetime.strptime(vote.timestamp, "%Y-%m-%dT%H:%M:%SZ"),
        biometric_hash=vote.biometric_hash
    )

    db.add(new_vote)
    
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate entry detected in the database!")

    # Notify WebSocket Clients
    for client in connected_clients:
        await client.send_json({"total_votes": db.query(Vote).count(), "votes": [v.__dict__ for v in db.query(Vote).all()]})

    return {"message": "Vote submitted successfully!"}

# Get All Votes
@app.get("/get_votes/")
async def get_votes(db: Session = Depends(get_db)):
    votes = db.query(Vote).all()
    return {"total_votes": len(votes), "votes": [v.__dict__ for v in votes]}

# WebSocket for Real-Time Updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()  # Keep the connection open
    except:
        connected_clients.remove(websocket)
