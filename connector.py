from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from firebase_admin import credentials, firestore, initialize_app

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Initialize Firestore
cred = credentials.Certificate("path/to/serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

# Pydantic model for request body
class User(BaseModel):
    name: str
    age: int
    city: str

# Create document endpoint
@app.post("/create")
async def create_document(user: User):
    db.collection("users").document(user.name).set(user.dict())
    return {"message": "Document created successfully"}

# Read document endpoint
@app.get("/read")
async def read_document():
    docs = db.collection("users").stream()
    data = {doc.id: doc.to_dict() for doc in docs}
    return data

# Update document endpoint
@app.post("/update")
async def update_document(user: User):
    doc_ref = db.collection("users").document(user.name)
    if doc_ref.get().exists:
        doc_ref.update(user.dict())
        return {"message": "Document updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Document not found")

# Delete document endpoint
@app.post("/delete")
async def delete_document(user: User):
    doc_ref = db.collection("users").document(user.name)
    if doc_ref.get().exists:
        doc_ref.delete()
        return {"message": "Document deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Document not found")
