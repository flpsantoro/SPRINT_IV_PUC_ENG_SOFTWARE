from flask import Blueprint, render_template, request, jsonify
from models.model_utils import predict
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@views.route('/predict', methods=['POST'])
def predict_route():
    #data = request.json
    data = pd.DataFrame({
        'hair': [0],
        'feathers': [0],
        'eggs': [1],
        'milk': [0],
        'airborne': [0],
        'aquatic': [1],
        'predator': [1],
        'toothed': [1],
        'backbone': [1],
        'breathes': [1],
        'venomous': [1],
        'fins': [0],
        'legs': [8],
        'tail': [0],
        'domestic': [0],
        'catsize': [0]
    })
    prediction = predict(data)
    return jsonify(prediction)
