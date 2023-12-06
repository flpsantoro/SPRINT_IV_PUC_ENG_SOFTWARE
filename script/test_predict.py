import pandas as pd
from joblib import load

model = load('svm_optimized_model.joblib')

dados = pd.DataFrame({
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

classes = pd.read_csv('datasets/class.csv')

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

classe_predict = model.predict(dados)[0]

print(mapear_numero_para_classe(classe_predict, classes))
