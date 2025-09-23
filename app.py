from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained model
model = joblib.load("mental_wellness.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            screen_time = float(request.form["screen_time"])
            sleep_hours = float(request.form["sleep_hours"])
            work_screen = float(request.form["work_screen"])

            features = np.array([[screen_time, sleep_hours, work_screen]])
            prediction = model.predict(features)[0]
            prediction = round(prediction, 2)
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
