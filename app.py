from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    duration = int(request.form["duration"])
    src_bytes = int(request.form["src_bytes"])
    dst_bytes = int(request.form["dst_bytes"])

    prediction = model.predict([[duration, src_bytes, dst_bytes]])

    if prediction[0] == 1:
        result = "Cyber Attack Detected"
    else:
        result = "Normal Traffic"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)