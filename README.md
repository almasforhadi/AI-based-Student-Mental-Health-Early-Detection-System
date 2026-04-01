# 🧠 Mental Health AI – Intelligent Student Mental Health Monitoring System

**Mental Health AI** is an AI-powered web platform developed using **Django and Machine Learning** to assist university students in assessing their mental well-being.
The system collects survey data related to lifestyle, behavioral patterns, and mental health indicators, and uses a **trained Machine Learning model** to predict the **mental health risk level** of students.

The platform provides **personal dashboards, AI-based risk analysis, and downloadable PDF reports**, while allowing administrators to monitor high-risk cases through a dedicated dashboard.

This project was developed as part of an **AI-based mental health early detection research thesis**.

---

# 🚀 Key Features

### 👤 User Features

* User registration and authentication
* Mental health survey system
* AI-based mental health risk prediction
* Personalized dashboard with risk insights
* Survey breakdown visualization
* Downloadable PDF mental health reports
* Educational mental health resources

### 🤖 AI & Machine Learning Features

* Survey data collection and dataset generation
* Data preprocessing for machine learning
* Mental health risk prediction using a **Random Forest ML model**
* Model training using collected survey data
* Saved trained model (`.pkl`) for real-time prediction
* AI-based classification of risk levels:

  * **Low Risk**
  * **Medium Risk**
  * **High Risk**

### 🛡 Admin Features

* Admin dashboard for monitoring student risk levels
* View high-risk students
* System-wide survey analytics
* Data monitoring for early intervention

---

# 🧠 AI / Machine Learning Pipeline

The platform integrates a machine learning workflow for predictive analysis:

```
Student Survey
      │
      ▼
Django Database (SurveyResponse)
      │
      ▼
Dataset Export (CSV)
      │
      ▼
Data Preprocessing
      │
      ▼
Machine Learning Training
(Random Forest Classifier)
      │
      ▼
Saved Model (.pkl)
      │
      ▼
AI Prediction
      │
      ▼
Risk Level Display on Dashboard
```

The trained model predicts the mental health risk level based on features such as:

* Sleep duration
* Device usage
* Emotional interest level
* Anxiety level
* Social feeling
* Self-rating

---

# 🛠 Tech Stack

### Backend

* **Django 6.x**
* Python 3.10+

### Machine Learning

* **Scikit-Learn**
* Random Forest Classifier
* Pandas (data processing)
* NumPy

### Frontend

* Django Templates
* Bootstrap 5
* Crispy Forms

### Database

* SQLite (default)

### PDF Generation

* ReportLab

### Authentication

* Django built-in authentication system

---

# 📂 Project Structure

```
mental_health_ai/
│
├── accounts/          # User authentication and profile management
├── survey/            # Survey models, forms, views
├── dashboard/         # User dashboard and admin analytics
├── reports/           # PDF report generation
│
├── ml_model/          # Machine Learning components
│   ├── export_dataset.py
│   ├── train_model.py
│   ├── predict.py
│   ├── survey_dataset.csv
│   └── risk_model.pkl
│
├── templates/         # HTML templates
├── static/            # CSS, JS, images
├── mental_health_ai/  # Django project settings
└── manage.py
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```
git clone https://github.com/<your-username>/mental_health_ai.git
cd mental_health_ai
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Apply Database Migrations

```
python manage.py migrate
```

---

## 5️⃣ Create Admin User

```
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000
```

---

# 🤖 Training the AI Model

Export survey data:

```
python ml_model/export_dataset.py
```

Train machine learning model:

```
python ml_model/train_model.py
```

This will:

* Train the **Random Forest classifier**
* Generate the trained model file

```
ml_model/risk_model.pkl
```

The saved model is automatically used for **real-time risk prediction** inside Django.

---

# 📝 System Usage

### Student Workflow

1. Register or login
2. Complete the mental health survey
3. AI model predicts risk level
4. View personalized dashboard
5. Generate mental health report

### Admin Workflow

1. Login as administrator
2. Access **/admin-panel/**
3. Monitor high-risk students
4. Review system statistics

---

# 📊 Example Prediction

Example student input:

```
Sleep Hours: < 5
Device Usage: 6+ hours
Anxiety Level: High
Interest Level: Low
Social Feeling: Isolated
Self Rating: Low
```

AI Prediction:

```
Risk Level: HIGH
```

---

# 📄 Deployment (Render / Production)

Push project to GitHub:

```
git add .
git commit -m "Initial AI-based mental health system"
git push origin main
```

Deploy using **Render Web Service**

**Build Command**

```
pip install -r requirements.txt && python manage.py migrate
```

**Start Command**

```
gunicorn mental_health_ai.wsgi
```

Environment Variables:

```
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=your-render-domain
```

---

# 📚 Research Context

This project was developed as part of a research thesis on:

**AI-based Early Detection of Mental Health Risks among University Students**

The system demonstrates how **machine learning models can assist in early mental health risk identification using behavioral survey data.**

---

# 👤 Author

**Md Almas Forhadi**

GitHub
https://github.com/<your-username>

---

# 📄 License

This project is licensed under the **MIT License**.
