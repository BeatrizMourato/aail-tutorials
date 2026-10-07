from flask import Flask, request, jsonify
import joblib
import numpy as np
# Load trained model
model = joblib.load("model.pkl")
app = Flask(__name__)
@app.route("/predict", methods=["POST"])
@app.route('/predict-batch', methods=['POST'])
def predict_batch():
    data = request.json['features']
    # Sem os parênteses retos [] à volta do data!
    predictions = model.predict(data)
    
    # Devolvemos "predictions" (no plural) como o teste espera
    return jsonify({"predictions": predictions.tolist()})
def predict():
 data = request.json["features"]
 prediction = model.predict([np.array(data)])
 return jsonify({"prediction": int(prediction[0])})
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8000)