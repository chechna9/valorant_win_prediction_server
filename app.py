from flask import Flask, request, jsonify
from model_dep import m2_feature_selection
from flask_cors import CORS
import pickle
import __main__

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
__main__.m2_feature_selection = m2_feature_selection

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Valorant Prediction API</h1>'''


@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve the input data from the request
    data = request.json['data']
    loaded_model = pickle.load(open("./finalized_model.sav", 'rb'))
    # Perform prediction using your logistic regression model
    prediction = loaded_model.predict_proba(data)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0][1]})
if __name__ == '__main__':
    app.run(debug=True)