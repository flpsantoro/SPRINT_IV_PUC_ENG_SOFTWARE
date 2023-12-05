from flask import Blueprint, render_template, request, jsonify
from models.model_utils import predict

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@views.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    prediction = predict(data)
    return jsonify(prediction)
