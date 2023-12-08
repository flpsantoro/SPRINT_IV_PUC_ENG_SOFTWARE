import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})
    return app.test_client()


def test_predict_route(client):
    dados_teste = {
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

    resposta = client.post('/predict', json=dados_teste)

    assert resposta.status_code == 200
    assert 'Mamíferos' in resposta.data.decode()
