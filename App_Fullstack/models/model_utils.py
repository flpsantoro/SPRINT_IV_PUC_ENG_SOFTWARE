import os
import joblib

model = None

# Verifique se o modelo existe antes de carregá-lo
if os.path.exists('models/model.pkl'):
    model = joblib.load('models/model.pkl')

def predict(data):
    # Certifique-se de que o modelo está carregado
    if model is not None:
        prediction = model.predict([data])
        return prediction
    else:
        # Retorne uma mensagem ou valor padrão se o modelo não estiver disponível
        return "Modelo não disponível"
