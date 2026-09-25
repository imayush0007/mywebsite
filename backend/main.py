from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import cursor, conn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Contact(BaseModel):
    name: str
    email: str
    message: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Ayush Rai Portfolio Backend 🚀"
    }


@app.post("/contact")
def save_contact(contact: Contact):

    print("NEW MESSAGE:", contact.name, contact.email)

    cursor.execute(
        "INSERT INTO contacts(name,email,message) VALUES(?,?,?)",
        (contact.name, contact.email, contact.message)
    )

    conn.commit()

    return {
        "message": "Message Saved Successfully!"
    }


@app.get("/messages")
def get_messages():

    new_cursor = conn.cursor()   # Naya cursor banao

    new_cursor.execute(
        "SELECT id, name, email, message FROM contacts ORDER BY id DESC"
    )

    rows = new_cursor.fetchall()

    messages = []

    for row in rows:
        messages.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "message": row[3]
        })

    new_cursor.close()   # Cursor close karo

    return messages
@app.delete("/delete/{message_id}")
def delete_message(message_id: int):

    new_cursor = conn.cursor()

    new_cursor.execute(
        "DELETE FROM contacts WHERE id=?",
        (message_id,)
    )

    conn.commit()
    new_cursor.close()

    return {
        "message": "Message Deleted Successfully!"
    }