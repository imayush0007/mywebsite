# ==========================================
# AYUSH RAI AI PORTFOLIO BACKEND (SECURE V9)
# ==========================================

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
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

# ---------- Admin Login ----------
ADMIN_USERNAME = "AyushAdmin"
ADMIN_PASSWORD = "Ayush@8360"

def verify_admin(password: str | None):
    if password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Unauthorized")

# ---------- Models ----------
class Contact(BaseModel):
    name: str
    email: str
    message: str


class Login(BaseModel):
    username: str
    password: str


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
def get_messages(x_admin_password: str = Header(None)):

    verify_admin(x_admin_password)

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
def delete_message(
    message_id: int,
    x_admin_password: str = Header(None)
):

    verify_admin(x_admin_password)

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


# ---------- Dashboard Login Page ----------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_login():

    return """
<!DOCTYPE html>
<html>
<head>
<meta charset='UTF-8'>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Ayush Dashboard Login</title>

<style>
body{
background:#020617;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
font-family:Arial,sans-serif;
margin:0;
}

.login-box{
background:#0f172a;
padding:40px;
border-radius:20px;
width:340px;
text-align:center;
border:1px solid #38bdf8;
box-shadow:0 0 30px rgba(56,189,248,.3);
}

h1{
color:#38bdf8;
margin-bottom:25px;
}

input{
width:100%;
padding:14px;
margin:10px 0;
border:none;
border-radius:10px;
background:#1e293b;
color:white;
font-size:15px;
}

button{
width:100%;
padding:14px;
margin-top:20px;
border:none;
border-radius:10px;
background:#0ea5e9;
color:white;
font-size:17px;
cursor:pointer;
}

button:hover{
background:#0284c7;
}

#error{
margin-top:15px;
color:#ef4444;
font-size:14px;
}
</style>

</head>

<body>

<div class="login-box">

<h1>🔒 Ayush Rai Private Dashboard</h1>

<p style="color:#94A3B8;">
Authorized access only.
</p>

<input id="username" placeholder="Username">

<input id="password" type="password" placeholder="Password">

<button onclick="login()">Login</button>

<p id="error"></p>

</div>

<script>

async function login(){

const username=document.getElementById("username").value;
const password=document.getElementById("password").value;

const response=await fetch("/login",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({username,password})
});

if(response.ok){
window.location="/dashboard/messages";
}else{
document.getElementById("error").innerHTML="❌ Invalid Username or Password";
}

}

</script>

</body>
</html>
"""


# ---------- Login API ----------
@app.post("/login")
def login(data: Login):

    if (
        data.username == ADMIN_USERNAME
        and data.password == ADMIN_PASSWORD
    ):
        return {"success": True}

    raise HTTPException(
        status_code=401,
        detail="Invalid Username or Password"
    )


# ---------- Protected Dashboard ----------
@app.get("/dashboard/messages", response_class=HTMLResponse)
def dashboard_messages():

    with open("dashboard.html", "r", encoding="utf-8") as file:
        html = file.read()

    return HTMLResponse(html)
