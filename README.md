
# 🌱 Crop Recommendation System using Machine Learning

A Machine Learning based web application built with **Python**, **Flask**, and **Scikit-learn** that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions.

---

# 📌 Project Overview

The Crop Recommendation System helps farmers and agriculture enthusiasts identify the most appropriate crop for cultivation. The application uses a trained Machine Learning model to analyze soil composition and climatic conditions before recommending the best crop.

Users simply enter values such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH level, and Rainfall through a web interface. The trained model processes these inputs and predicts the most suitable crop.

This project demonstrates the practical use of Machine Learning in smart agriculture.

---

# 🎯 Objective

The objective of this project is to assist farmers in selecting the best crop based on environmental and soil parameters, helping improve productivity and reduce poor crop selection.

---

# ✨ Features

* 🌾 Crop recommendation using Machine Learning
* 🌡 Predicts crop based on environmental conditions
* 🧪 Uses soil nutrient values (N, P, K)
* 💧 Considers rainfall and humidity
* 📊 Data preprocessing using StandardScaler
* ⚡ Fast prediction using a trained classification model
* 🖥 User-friendly Flask web interface

---

# 🛠 Technologies Used

* Python
* Flask
* NumPy
* Scikit-learn
* Pickle
* HTML
* CSS

---

# 🤖 Machine Learning Model

The application uses a trained classification model stored as **vc.pkl**.

Input features are first normalized using **StandardScaler (ss.pkl)** before being passed to the prediction model.

The model predicts one of the supported crop names directly.

---

# 📂 Project Structure

```text
Crop-Recommendation-System/
│── app.py
│── vc.pkl
│── ss.pkl
│── templates/
│     └── index.html
│── static/
│     ├── style.css
│     └── images/
│── requirements.txt
└── README.md
```

---

# 📥 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Crop-Recommendation-System.git
```

Move into the project directory:

```bash
cd Crop-Recommendation-System
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Run the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

# 📖 How It Works

1. User enters soil and weather information.
2. Flask receives the input values.
3. The StandardScaler preprocesses the data.
4. The trained Machine Learning model predicts the most suitable crop.
5. The recommended crop is displayed on the webpage.

---

# 📊 Input Parameters

The prediction is based on the following inputs:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Value
* Rainfall

---

# 🌾 Output

The system predicts crops such as:

* Rice
* Maize
* Cotton
* Coconut
* Banana
* Mango
* Grapes
* Apple
* Orange
* Papaya
* Coffee
* Chickpea
* Lentil
* Mothbeans
* Mungbean
* Pigeonpeas
* Kidneybeans
* Watermelon
* Muskmelon
* Pomegranate
* Jute
* Blackgram

---

# 📦 Required Files

* app.py
* vc.pkl
* ss.pkl
* templates/index.html
* requirements.txt

---

# 🚀 Future Improvements

* Fertilizer recommendation
* Crop yield prediction
* Disease detection
* Weather API integration
* Soil image analysis
* Mobile-friendly interface
* Cloud deployment
* Multi-language support

---

# 👨‍💻 Author

Developed using **Python**, **Flask**, and **Machine Learning** for smart agriculture and educational purposes.

---

# 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it for educational and personal learning purposes.
