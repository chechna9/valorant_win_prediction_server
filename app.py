from flask import Flask, request, jsonify
from model_dep import *
import pickle

app = Flask(__name__)
loaded_model = pickle.load(open("./log_reg_model.pkl", "rb"))
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Valorant Prediction API</h1>'''
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input data from the request
    data = request.json['data']
    
    # Perform prediction using your logistic regression model
    prediction = loaded_model.predict([data])[0]
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})
if __name__ == '__main__':
    app.run(debug=True)