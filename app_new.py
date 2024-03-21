
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origin or "*" to allow all origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Add "OPTIONS" method
    allow_headers=["*"],
)
@app.get("/login")
async def login(email: str = Query(..., description="User email"), password: str = Query(..., description="User password")):
    # Your authentication logic goes here
    if email == "a@abc.com" and password == "abc":
        return {"message": "Login successful"}
    else:
        return {"message": "Login failed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)