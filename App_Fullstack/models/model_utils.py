import os
import joblib
import pandas as pd

model = None
classes = None

if os.path.exists('models/svm_optimized_model.joblib'):
    model = joblib.load('models/svm_optimized_model.joblib')

if os.path.exists('models/datasets/class.csv'):
    classes = pd.read_csv('models/datasets/class.csv')

def mapear_numero_para_classe(numero_classe, class_data):
    """
    Mapeia o número da classe para o nome da classe usando o DataFrame class_data.

    :param numero_classe: O número da classe prevista pelo modelo.
    :param class_data: DataFrame contendo o mapeamento de números de classe para nomes de classe.
    :return: O nome da classe correspondente.
    """
    class_row = class_data[class_data['Class_Number'] == numero_classe]
    if not class_row.empty:
        return class_row.iloc[0]['Class_Type']
    else:
        return "Classe não encontrada"

def predict(data):
    if model is not None:
        prediction = model.predict(data)
        result = mapear_numero_para_classe(prediction[0], classes)
        return result
    else:
        return "Modelo não disponível"
