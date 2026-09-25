// ==========================================
// AYUSH RAI AI PORTFOLIO V5 - FIXED
// ==========================================

// ---------- PAGE LOAD ----------
window.addEventListener("load", () => {

  const loader = document.getElementById("loader");

  if (loader) {
    setTimeout(() => {
      loader.style.opacity = "0";
      loader.style.transition = "0.5s";
      setTimeout(() => loader.style.display = "none", 500);
    }, 1500);
  }

  updateClock();
  setInterval(updateClock, 1000);

  visitorCounter();
  animateSkills();
  createParticles();
  typingEffect();
});

// ---------- LIVE INDIA CLOCK ----------
function updateClock() {

  const clock = document.getElementById("clock");
  if (!clock) return;

  clock.innerHTML = new Date().toLocaleString("en-IN", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: true,
    timeZone: "Asia/Kolkata"
  });

}

// ---------- VISITOR COUNTER ----------
function visitorCounter() {

  let visits = Number(localStorage.getItem("ayushPortfolioVisitors")) || 0;

  visits++;

  localStorage.setItem("ayushPortfolioVisitors", visits);

  const counter = document.getElementById("visitor-count");

  if (counter) counter.innerText = visits;

}

// ---------- TYPING EFFECT ----------
const words = [
  "AI/ML Student",
  "Python Developer",
  "Machine Learning Enthusiast",
  "FastAPI Developer",
  "Future AI Engineer"
];

let wordIndex = 0;
let charIndex = 0;
let deleting = false;

function typingEffect() {

  const text = document.getElementById("typing-text");
  if (!text) return;

  const current = words[wordIndex];

  if (!deleting) {

    text.innerHTML = current.substring(0, charIndex++);

    if (charIndex > current.length) {
      deleting = true;
      setTimeout(typingEffect, 1200);
      return;
    }

  } else {

    text.innerHTML = current.substring(0, charIndex--);

    if (charIndex < 0) {
      deleting = false;
      wordIndex = (wordIndex + 1) % words.length;
    }

  }

  setTimeout(typingEffect, deleting ? 40 : 90);

}

// ---------- SKILLS ----------
function animateSkills() {

  document.querySelectorAll(".progress-bar").forEach(bar => {
    setTimeout(() => {
      bar.style.width = bar.dataset.width;
    }, 500);
  });

}

// ---------- PARTICLES ----------
function createParticles() {

  const canvas = document.getElementById("particles");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");

  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const particles = [];

  for (let i = 0; i < 100; i++) {

    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      r: Math.random() * 3 + 1,
      dx: (Math.random() - 0.5) * 1.5,
      dy: (Math.random() - 0.5) * 1.5
    });

  }

  function draw() {

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = "#38bdf8";

    particles.forEach(p => {

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fill();

      p.x += p.dx;
      p.y += p.dy;

      if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
      if (p.y < 0 || p.y > canvas.height) p.dy *= -1;

    });

    requestAnimationFrame(draw);

  }

  draw();

}

// ---------- CURSOR ----------
const cursor = document.querySelector(".cursor");

document.addEventListener("mousemove", e => {

  if (!cursor) return;

  cursor.style.left = e.clientX + "px";
  cursor.style.top = e.clientY + "px";

});

// ---------- SCROLL BAR ----------
window.addEventListener("scroll", () => {

  const progress = document.getElementById("progressBar");
  if (!progress) return;

  const value =
    window.scrollY /
    (document.body.scrollHeight - window.innerHeight);

  progress.style.width = value * 100 + "%";

});

// ---------- BACK TO TOP ----------
const topBtn = document.getElementById("topBtn");

window.addEventListener("scroll", () => {

  if (!topBtn) return;

  topBtn.style.display =
    window.scrollY > 400 ? "block" : "none";

});

if (topBtn) {

  topBtn.onclick = () => {

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });

  };

}

// ---------- AI CHATBOT ----------
function toggleChat() {

  const chat = document.getElementById("chatBox");

  if (!chat) return;

  chat.style.display =
    chat.style.display === "flex" ? "none" : "flex";

}

function sendMessage() {

  const input = document.getElementById("chatInput");
  const body = document.getElementById("chatBody");

  if (!input || !body) return;

  const message = input.value.trim();
  if (message === "") return;

  body.innerHTML += `<div class="user">${message}</div>`;

  let reply = "🤖 I'm Ayush's AI Assistant.";

  const text = message.toLowerCase();

  if (text.includes("hello") || text.includes("hi"))
    reply = "👋 Hello Ayush! Welcome to your AI Portfolio.";

  else if (text.includes("skills"))
    reply = "💻 Python, ML, SQL, HTML, CSS, JavaScript and FastAPI.";

  else if (text.includes("project"))
    reply = "🚀 AI Chatbot, Student Predictor, FastAPI Dashboard and Portfolio Website.";

  else if (text.includes("resume"))
    reply = "📄 Click the Resume button to preview your resume.";

  else if (text.includes("contact"))
    reply = "📧 Email: raiayush2003.2021@gmail.com";

  setTimeout(() => {

    body.innerHTML += `<div class="bot">${reply}</div>`;

    body.scrollTop = body.scrollHeight;

  }, 400);

  input.value = "";

}

const chatInput = document.getElementById("chatInput");

if (chatInput) {

  chatInput.addEventListener("keypress", e => {

    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }

  });

}

// ---------- RESUME ----------
function openResume() {

  const modal = document.getElementById("resumeModal");
  if (modal) modal.style.display = "flex";

}

function closeResume() {

  const modal = document.getElementById("resumeModal");
  if (modal) modal.style.display = "none";

}

// ---------- DARK MODE ----------
function toggleTheme() {

  document.body.classList.toggle("light-mode");

  const btn = document.getElementById("themeBtn");

  if (btn) {
    btn.innerHTML =
      document.body.classList.contains("light-mode")
        ? "☀️"
        : "🌙";
  }

}

// ---------- CONTACT FORM (RENDER LIVE) ----------
const form = document.getElementById("contact-form");

if (form) {
  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
      name: document.getElementById("name").value.trim(),
      email: document.getElementById("email").value.trim(),
      message: document.getElementById("message").value.trim()
    };

    if (!data.name || !data.email || !data.message) {
      alert("⚠️ Please fill all fields.");
      return;
    }

    try {
      const response = await fetch("https://ayush-ai-backend.onrender.com/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();

      if (response.ok) {
        alert("✅ " + result.message);
        form.reset();
      } else {
        alert("❌ Failed to send message.");
      }

    } catch (error) {
      console.error(error);
      alert("❌ Connection Error. Please try again.");
    }
  });
}
// ---------- MUSIC ----------
let playing = false;

function toggleMusic() {

  const music = document.getElementById("bgMusic");
  if (!music) return;

  if (!playing) {
    music.play();
    playing = true;
  } else {
    music.pause();
    playing = false;
  }

}

console.log("✅ Ayush AI Portfolio V5 Loaded Successfully");

// Disable Right Click
document.addEventListener("contextmenu", function (e) {
  e.preventDefault();
});

// Disable Inspect Shortcuts
document.addEventListener("keydown", function (e) {
  if (
    e.key === "F12" ||
    (e.ctrlKey && e.shiftKey && ["I", "J", "C"].includes(e.key)) ||
    (e.ctrlKey && e.key === "U")
  ) {
    e.preventDefault();
    alert("⚠️ Inspect/View Source is disabled.");
  }
});
