import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, make_scorer
from sklearn.pipeline import Pipeline
from joblib import dump
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados
class_data = pd.read_csv('datasets/class.csv')
zoo_data = pd.read_csv('datasets/zoo.csv')

# Preparando os dados
zoo_data_clean = zoo_data.drop('animal_name', axis=1)
X = zoo_data_clean.drop('class_type', axis=1)
y = zoo_data_clean['class_type']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definindo os pipelines e parâmetros para GridSearchCV
pipelines = {
    "Decision Tree": Pipeline([('scaler', StandardScaler()), ('model', DecisionTreeClassifier())]),
    "Random Forest": Pipeline([('scaler', StandardScaler()), ('model', RandomForestClassifier())]),
    "Logistic Regression": Pipeline([('scaler', StandardScaler()), ('model', LogisticRegression())]),
    "SVM": Pipeline([('scaler', StandardScaler()), ('model', SVC())]),
    "KNN": Pipeline([('scaler', StandardScaler()), ('model', KNeighborsClassifier())]),
    "Naive Bayes": Pipeline([('scaler', StandardScaler()), ('model', GaussianNB())])
}

param_grids = {
    "Decision Tree": {'model__max_depth': [None, 10, 20], 'model__min_samples_split': [2, 5, 10]},
    "Random Forest": {'model__n_estimators': [100, 200], 'model__max_depth': [None, 10, 20], 'model__min_samples_split': [2, 5]},
    "Logistic Regression": {'model__C': [0.1, 1, 10]},
    "SVM": {'model__C': [0.1, 1, 10], 'model__gamma': [0.001, 0.01]},
    "KNN": {'model__n_neighbors': [3, 5, 7], 'model__weights': ['uniform', 'distance']},
    "Naive Bayes": {}  # Naive Bayes geralmente tem poucos hiperparâmetros para ajustar
}

# Otimização de hiperparâmetros para cada modelo
optimized_models = {}
for name, pipeline in pipelines.items():
    grid_search = GridSearchCV(pipeline, param_grids[name], cv=10, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)  # Note que estamos usando todo o conjunto de dados aqui
    optimized_models[name] = grid_search.best_estimator_

# Avaliação dos modelos otimizados com validação cruzada de 10-folds
cv_scores = {}
for name, model in optimized_models.items():
    accuracy = cross_val_score(model, X, y, cv=10, scoring=make_scorer(accuracy_score))
    recall = cross_val_score(model, X, y, cv=10, scoring=make_scorer(recall_score, average='weighted'))
    f1 = cross_val_score(model, X, y, cv=10, scoring=make_scorer(f1_score, average='weighted'))

    cv_scores[name] = {
        'CV Accuracy Mean': np.mean(accuracy),
        'CV Recall Mean': np.mean(recall),
        'CV F1 Score Mean': np.mean(f1)
    }

# Exibindo os resultados
df_cv_scores = pd.DataFrame(cv_scores).T
print(df_cv_scores)

# Exportando o melhor modelo baseado na média da acurácia de CV
best_model_name = max(cv_scores, key=lambda name: cv_scores[name]['CV Accuracy Mean'])
best_model = optimized_models[best_model_name]
model_filename = f'{best_model_name.lower()}_optimized_model.joblib'
dump(best_model, model_filename)

# Visualização dos resultados
plt.figure(figsize=(12, 8))
sns.barplot(x=df_cv_scores.index, y=df_cv_scores['CV Accuracy Mean'])
plt.title('Comparação de Acurácia Média dos Modelos com Validação Cruzada de 10-folds')
plt.ylabel('Acurácia Média')
plt.xlabel('Modelos')
plt.xticks(rotation=45)
plt.show()