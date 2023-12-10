from unittest.mock import patch

import pandas as pd

import pytest
from flask import Flask

from routes.views import views


class TestPredictRoute:


    def test_valid_post_request(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()
        data = {
            'hair': 1,
            'feathers': 0,
            'eggs': 0,
            'milk': 0,
            'airborne': 0,
            'aquatic': 0,
            'predator': 0,
            'toothed': 1,
            'backbone': 1,
            'breathes': 1,
            'venomous': 0,
            'fins': 0,
            'legs': 4,
            'tail': 1,
            'domestic': 1,
            'catsize': 0
        }

        # Act
        response = client.post('/predict', json=data)
        result = response.get_json()

        # Assert
        assert response.status_code == 200
        assert 'Modelo não disponível' in result

    def test_call_predict_function(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()
        data = {
            'hair': 1,
            'feathers': 0,
            'eggs': 0,
            'milk': 0,
            'airborne': 0,
            'aquatic': 0,
            'predator': 0,
            'toothed': 1,
            'backbone': 1,
            'breathes': 1,
            'venomous': 0,
            'fins': 0,
            'legs': 4,
            'tail': 1,
            'domestic': 1,
            'catsize': 0
        }

        # Act
        with patch('views.predict') as mock_predict:
            response = client.post('/predict', json=data)

        # Assert
        mock_predict.assert_called_once_with(pd.DataFrame([data]))

    def test_create_dataframe(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()
        data = {
            'hair': 1,
            'feathers': 0,
            'eggs': 0,
            'milk': 0,
            'airborne': 0,
            'aquatic': 0,
            'predator': 0,
            'toothed': 1,
            'backbone': 1,
            'breathes': 1,
            'venomous': 0,
            'fins': 0,
            'legs': 4,
            'tail': 1,
            'domestic': 1,
            'catsize': 0
        }

        # Act
        with patch('views.pd.DataFrame') as mock_dataframe:
            response = client.post('/predict', json=data)

        # Assert
        mock_dataframe.assert_called_once_with([data])

    def test_invalid_post_request(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()

        # Act
        response = client.post('/predict')
        result = response.get_json()

        # Assert
        assert response.status_code == 400
        assert 'error' in result

    def test_predict_function_error(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()
        data = {
            'hair': 1,
            'feathers': 0,
            'eggs': 0,
            'milk': 0,
            'airborne': 0,
            'aquatic': 0,
            'predator': 0,
            'toothed': 1,
            'backbone': 1,
            'breathes': 1,
            'venomous': 0,
            'fins': 0,
            'legs': 4,
            'tail': 1,
            'domestic': 1,
            'catsize': 0
        }

        # Act
        with patch('views.predict') as mock_predict:
            mock_predict.return_value = "Modelo não disponível"
            response = client.post('/predict', json=data)
            result = response.get_json()

        # Assert
        assert response.status_code == 400
        assert 'error' in result

    def test_invalid_data_type(self):
        # Arrange
        app = Flask(__name__)
        app.register_blueprint(views)
        client = app.test_client()
        data = 'invalid_data'

        # Act
        response = client.post('/predict', json=data)
        result = response.get_json()

        # Assert
        assert response.status_code == 400
        assert 'error' in result
