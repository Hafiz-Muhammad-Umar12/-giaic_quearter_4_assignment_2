from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --------------------------
# In-memory "database"
# --------------------------
users = [
    {"name": "Ali", "pin": "1234", "balance": 1000},
    {"name": "Umar", "pin": "4321", "balance": 500},
]


# --------------------------
# Request Schemas
# --------------------------
class AuthRequest(BaseModel):
    name: str
    pin_number: str


class TransferRequest(BaseModel):
    sender_name: str
    receiver_name: str
    amount: float


# --------------------------
# /authenticate
# --------------------------

@app.get("/")
def home():
    return {"message": "Bank API Running Successfully!"}
    
@app.post("/authenticate")
def authenticate(data: AuthRequest):
    for user in users:
        if user["name"] == data.name and user["pin"] == data.pin_number:
            return {
                "message": "Authenticated Successfully",
                "user": user
            }

    raise HTTPException(status_code=401, detail="Invalid name or pin")


# --------------------------
# /bank-transfer
# --------------------------
@app.post("/bank-transfer")
def bank_transfer(req: TransferRequest):
    sender = next((u for u in users if u["name"] == req.sender_name), None)
    receiver = next((u for u in users if u["name"] == req.receiver_name), None)

    if not sender or not receiver:
        raise HTTPException(status_code=404, detail="Sender or Receiver not found")

    if sender["balance"] < req.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    # Transfer process
    sender["balance"] -= req.amount
    receiver["balance"] += req.amount

    return {
        "message": "Transfer Successful",
        "sender": sender,
        "receiver": receiver
    }
