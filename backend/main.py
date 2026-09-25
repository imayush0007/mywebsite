# ==========================================
# AYUSH RAI AI PORTFOLIO BACKEND (RENDER LIVE)
# ==========================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import conn

app = FastAPI(title="Ayush AI Portfolio Backend")

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://imayush0007.github.io",
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Contact Model ----------
class Contact(BaseModel):
    name: str
    email: str
    message: str


# ---------- Home ----------
@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Welcome to Ayush Rai AI Portfolio Backend 🚀"
    }


# ---------- Save Contact ----------
@app.post("/contact")
def save_contact(contact: Contact):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name,email,message) VALUES(?,?,?)",
        (contact.name, contact.email, contact.message)
    )

    conn.commit()
    cursor.close()

    return {
        "status": "success",
        "message": "Message Saved Successfully!"
    }


# ---------- Get Messages ----------
@app.get("/messages")
def get_messages():

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, message FROM contacts ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    cursor.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "message": row[3]
        }
        for row in rows
    ]


# ---------- Delete Message ----------
@app.delete("/delete/{message_id}")
def delete_message(message_id: int):

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id=?",
        (message_id,)
    )

    conn.commit()
    cursor.close()

    return {
        "status": "success",
        "message": "Message Deleted Successfully!"
    }
