from flask import Blueprint, render_template, request, jsonify
from models.model_utils import predict
import pandas as pd

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@views.route('/predict', methods=['POST'])
def predict_route():
    request_data = request.json
    data = pd.DataFrame([request_data])
    prediction = predict(data)
    return jsonify(prediction)
