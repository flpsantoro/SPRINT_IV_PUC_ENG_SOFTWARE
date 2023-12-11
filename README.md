# Pós-Graduação em Engenharia de Software - PUC Rio

## Sobre o Projeto
Este projeto é parte de um MVP (Produto Mínimo Viável) desenvolvido para o curso de pós-graduação em Engenharia de Software da PUC Rio. Ele inclui o desenvolvimento e a implementação de um modelo de machine learning para classificação, bem como a criação de uma aplicação full stack integrando o modelo.

## Estrutura do Repositório
- `App_Fullstack`: Contém os códigos fonte da aplicação full stack desenvolvida.
- `Notebook`: Inclui o notebook no Google Colab utilizado para o desenvolvimento do modelo de machine learning.

## Modelo de Machine Learning
O modelo de machine learning foi desenvolvido seguindo as etapas de carga de dados, separação entre treino e teste, transformação de dados, modelagem, otimização de hiperparâmetros, avaliação e comparação de resultados. Algoritmos como KNN, Árvore de Classificação, Naive Bayes e SVM foram utilizados.

## Aplicação Full Stack
A aplicação full stack permite a entrada de novos dados para predição utilizando o modelo de classificação. Esta parte cobre tanto o back-end (carga do modelo) quanto o front-end (interface de usuário para entrada de dados e exibição de resultados).

## Testes Automatizados
Utilizando PyTest, foram implementados testes automatizados para assegurar o desempenho do modelo de machine learning de acordo com os requisitos estabelecidos.

## Boas Práticas de Desenvolvimento Seguro
Reflexões sobre a aplicação de boas práticas de desenvolvimento seguro, como anonimização de dados, foram consideradas no projeto.

## Execução
Para executar o notebook de machine learning:
- Acesse a pasta `Notebook` e abra o arquivo Jupyter no Google Colab.

Para rodar a aplicação full stack:
- Navegue até a pasta `App_Fullstack` e execute a aplicação `app.py` em flask
