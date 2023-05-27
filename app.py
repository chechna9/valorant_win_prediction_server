from flask import Flask, request, jsonify
from model_dep import *
from flask_cors import CORS
import pickle

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
loaded_model = pickle.load(open("./finalized_model.sav", 'rb'))
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Valorant Prediction API</h1>'''


@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input data from the request
    data = request.json['data']
    # Perform prediction using your logistic regression model
    prediction = loaded_model.predict_proba(data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0][1]})
if __name__ == '__main__':
    app.run(debug=True)