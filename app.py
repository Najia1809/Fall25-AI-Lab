from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        val1 = float(request.form["val1"])
        val2 = float(request.form["val2"])
        val3 = float(request.form["val3"])

        # Convert input to array
        input_data = np.array([[val1, val2, val3]])

        # Make prediction
        pred = model.predict(input_data)[0]

        return render_template("index.html", prediction=pred)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
