import os
import joblib
import pandas as pd
import glob

model = None
classes = None

joblib_files = glob.glob('models/*.joblib')
if joblib_files:
    model = joblib.load(joblib_files[0])

if os.path.exists('models/datasets/class.csv'):
    classes = pd.read_csv('models/datasets/class.csv')


def mapear_numero_para_classe(numero_classe, class_data):
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
