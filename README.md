# 🧠 Mental Wellness Prediction App

This project is a **Flask web application** that predicts **mental wellness levels** based on lifestyle factors such as screen time, sleep hours, and work-related screen exposure.  
It uses a **Machine Learning model** trained in **Google Colab** and deployed via **Hugging Face Spaces** for public access.

---

## 🚀 Live Demo
👉 [Click here to try the app](https://jobanjps-Mental-Wellness.hf.space)

---

## 📌 Project Overview
The application allows users to input:
- 📱 **Screen Time (hours/day)**
- 😴 **Sleep Hours (hours/day)**
- 💻 **Work-related Screen Time (hours/day)**

Based on these inputs, the ML model predicts the **mental wellness score** of the user.

---

## 🛠️ Tech Stack
- **Frontend & Backend**: [Flask](https://flask.palletsprojects.com/)
- **Machine Learning Model**: Trained in [Google Colab](https://colab.research.google.com/drive/1MwHbFQsmL1PuD_epcWl6xjQEBdbEThDX#scrollTo=a54c4c28)  
- **Model Serialization**: `joblib`
- **Deployment**: [Hugging Face Spaces](https://huggingface.co/spaces)

---

## 📂 Repository Structure
```

Mental\_Wellness/
│
├── app.py                  # Flask application
├── mental\_wellness.pkl     # Trained ML model (serialized with joblib)
├── templates/
│   └── index.html          # Frontend (HTML form + result display)
├── static/                 # (Optional) CSS/JS files for styling
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

````

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Jobanjps089/Mental_Wellness.git
cd Mental_Wellness
````

### 2️⃣ Create & activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask app

```bash
python app.py
```

The app will be available at: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 📖 Usage

1. Open the app in your browser.
2. Enter:

   * Your **daily screen time** in hours.
   * Your **sleep duration** in hours.
   * Your **work-related screen time** in hours.
3. Click **Predict**.
4. The app will display your **predicted mental wellness score**.

---

## 🤖 Machine Learning Model

* Trained in **Google Colab**
* Dataset included features like screen time, sleep patterns, and work screen usage.
* Model was trained using **Scikit-learn** and saved as `mental_wellness.pkl` using **joblib**.
* The notebook can be found here: [Colab File](https://colab.research.google.com/drive/1MwHbFQsmL1PuD_epcWl6xjQEBdbEThDX#scrollTo=a54c4c28)

---

## 🌍 Deployment

The app is hosted on **Hugging Face Spaces**:
👉 [Mental Wellness App](https://jobanjps-Mental-Wellness.hf.space)

---

## 📷 Screenshots

### 🔹 Input Form

User inputs daily habits:

```
Screen Time: 6
Sleep Hours: 7
Work Screen: 5
```

### 🔹 Prediction Result

```
Predicted Mental Wellness Score: 7.45
```

---

## 📌 Requirements

The main dependencies are:

```
Flask
joblib
numpy
scikit-learn
```

---

## ⚡ Future Improvements

* Add more input features (exercise, diet, stress levels).
* Enhance UI with CSS/JS for a modern look.
* Integrate database for user history tracking.
* Deploy to cloud platforms like AWS/Azure/GCP for wider access.

---

## 👨‍💻 Author

**Jobanpreet Singh**
🔗 [GitHub Profile](https://github.com/Jobanjps089)

---

## 📜 License

This project is licensed under the **MIT License** - feel free to use and modify with attribution.

---
