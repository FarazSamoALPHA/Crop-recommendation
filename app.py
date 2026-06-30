from flask import Flask, request, render_template
import numpy as np
import pickle

# ===========================
# Load Model and Scaler
# ===========================

vc = pickle.load(open("vc.pkl", "rb"))
ss = pickle.load(open("ss.pkl", "rb"))

# ===========================
# Crop Dictionary
# ===========================

crop_dict = {
    1: "Rice",
    2: "Maize",
    3: "Jute",
    4: "Cotton",
    5: "Coconut",
    6: "Papaya",
    7: "Orange",
    8: "Apple",
    9: "Muskmelon",
    10: "Watermelon",
    11: "Grapes",
    12: "Mango",
    13: "Banana",
    14: "Pomegranate",
    15: "Lentil",
    16: "Blackgram",
    17: "Mungbean",
    18: "Mothbeans",
    19: "Pigeonpeas",
    20: "Kidneybeans",
    21: "Chickpea",
    22: "Coffee"
}

# ===========================
# Flask App
# ===========================

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        N = float(request.form["Nitrogen"])
        P = float(request.form["Phosporus"])
        K = float(request.form["Potassium"])
        temp = float(request.form["Temperature"])
        humidity = float(request.form["Humidity"])
        ph = float(request.form["Ph"])
        rainfall = float(request.form["Rainfall"])

        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])

        # Scale Features
        features = ss.transform(features)

        # Scale Features
        features = ss.transform(features)

        # Prediction
        prediction = vc.predict(features)

        crop = prediction[0]

        result = f"{crop.title()} is the best crop to be cultivated right there."

        return render_template("index.html", result=result)

        # # Prediction
        # prediction = vc.predict(features)
        #
        # predicted_label = int(prediction[0])
        #
        # if predicted_label in crop_dict:
        #     result = f"{crop_dict[predicted_label]} is the best crop to be cultivated right there."
        # else:
        #     result = "Prediction completed, but crop label not found."
        #
        # return render_template("index.html", result=result)

    except Exception as e:
        return render_template("index.html", result=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)