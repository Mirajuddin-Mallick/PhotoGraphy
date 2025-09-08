# Photography Portfolio Website 📸

A personal photography portfolio website built using **Flask**.  
It displays your profile, gallery, and contact form where users can send messages, and the messages are stored in an **SQLite database**.

---

## 🚀 Features
- 🖼️ Display profile photo and portfolio images
- 📩 Contact form with message storage
- 🗄️ Messages saved in **SQLite database**
- 🔍 Admin route to view all messages
- 📱 Fully responsive and mobile-friendly

---

## 🗂️ Project Structure
```
photography-website/
│── static/              # CSS, JS, Images
│    ├── photos/         # All portfolio images
│── templates/
│    ├── index.html      # Homepage template
│── messages.db          # SQLite database
│── app.py               # Flask backend
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/photography-website.git
cd photography-website
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # For Mac/Linux
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App
```bash
python app.py
```

The app will start at:  
**http://127.0.0.1:5000**

---

## 📨 View Stored Messages
Visit:
```
http://127.0.0.1:5000/admin/messages
```

---

## 📧 Enable Email Notifications (Optional)
To receive emails when someone submits a contact form, configure **Flask-Mail** in `app.py`.

---

## 📌 Requirements
- Python 3.8+
- Flask
- SQLite3

---

## 🏆 Author
**Mirajuddin Mallick**  
Professional Photographer & Developer  
