# E-Shop Brasil — Sistema Big Data com MongoDB, Streamlit e Docker

Esse é um projeto desenvolvido para a disciplina Advanced Databases and Big Data, com foco em uma solução prática usando MongoDB, Streamlit e Docker para simular os desafios da empresa fictícia E-Shop Brasil.

## Objetivo da Aplicação

A aplicação demonstra:

- Inserção de dados em banco NoSQL (MongoDB)
- Edição e exclusão de registros
- Concatenação de datasets utilizando Pandas
- Consultas e visualização em interface Streamlit
- Ambiente totalmente dockerizado com dois containers:
  - MongoDB
  - Streamlit App

## Tecnologias Utilizadas

- Python 3.10
- Streamlit
- MongoDB
- Docker e Docker Compose
- Pandas

## Estrutura do Projeto

├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── exemplos/
│ ├── insercao.png
│ ├── consulta.png
│ ├── edicao.png
│ ├── exclusao.png
│ └── concatenacao.png
└── README.md

## Como executar o projeto

### 1) Clonar o repositório.
### 2) Abrir o terminal e executar:

docker-compose up --build

## Acessar localmente

http://localhost:8501



