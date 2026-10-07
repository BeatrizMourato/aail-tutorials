from flask import Flask, request, jsonify
import joblib
import numpy as np
# Load trained model
model = joblib.load("model.pkl")
app = Flask(__name__)

#def predict():
 #data = request.json["features"]
 #prediction = model.predict([np.array(data)])
 #return jsonify({"prediction": int(prediction[0])})

 
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    # O predict normal PRECISA dos [] à volta do data
    prediction = model.predict([data])
    return jsonify({"prediction": prediction.tolist()})

@app.route('/predict-batch', methods=['POST'])
def predict_batch():
    data = request.json['features']
    # O batch NÃO PODE TER os [], usa apenas data
    predictions = model.predict(data)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
 app.run(host="0.0.0.0", port=8000)