from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    duration = int(request.form['duration'])
    src_bytes = int(request.form['src_bytes'])
    dst_bytes = int(request.form['dst_bytes'])

    prediction = model.predict([[duration, src_bytes, dst_bytes]])

    if prediction[0] == 1:
        result = "Cyber Attack Detected"
    else:
        result = "Normal Traffic"

    return render_template("index.html", result=result)

app.run(debug=True)