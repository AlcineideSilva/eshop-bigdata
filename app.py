import streamlit as st
from pymongo import MongoClient
import pandas as pd
from bson import ObjectId

# Conexão com MongoDB

client = MongoClient("mongodb://mongodb:27017/")
db = client["eshop"]
collection = db["clientes"]

st.title("📊 E-Shop Brasil — Sistema de Gestão de Dados")

menu = st.sidebar.selectbox("Menu", ["Inserir Dados", "Editar Dados", "Excluir Dados", "Concatenar Dados", "Consultar Dados"])

# FUNÇÃO PARA CONVERTER ObjectId PARA STRING

def fix_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# INSERIR DADOS

if menu == "Inserir Dados":
    st.subheader("Inserção de Dados no MongoDB")

    nome = st.text_input("Nome do Cliente")
    email = st.text_input("Email")
    compras = st.number_input("Quantidade de Compras", min_value=0)

    if st.button("Salvar"):
        collection.insert_one({
            "nome": nome,
            "email": email,
            "compras": compras
        })
        st.success("Dados inseridos com sucesso!")

# EDITAR DADOS

elif menu == "Editar Dados":
    st.subheader("Editar Registros")

    data = list(collection.find())
    if not data:
        st.info("Nenhum dado encontrado.")
    else:
        df = pd.DataFrame([fix_id(x) for x in data])
        selecionado = st.selectbox("Selecione o ID para editar", df["_id"])

        novo_nome = st.text_input("Novo nome")
        novo_email = st.text_input("Novo email")

        if st.button("Atualizar"):
            collection.update_one(
                {"_id": ObjectId(selecionado)},
                {"$set": {"nome": novo_nome, "email": novo_email}}
            )
            st.success("Registro atualizado com sucesso!")

# EXCLUIR DADOS

elif menu == "Excluir Dados":
    st.subheader("Excluir Registros")

    data = list(collection.find())
    if not data:
        st.info("Nenhum dado encontrado.")
    else:
        df = pd.DataFrame([fix_id(x) for x in data])
        selecionado = st.selectbox("Selecione o ID para excluir", df["_id"])

        if st.button("Excluir"):
            collection.delete_one({"_id": ObjectId(selecionado)})
            st.success("Registro excluído com sucesso!")

# CONCATENAR DADOS

elif menu == "Concatenar Dados":
    st.subheader("Concatenar Dados (Pandas + MongoDB)")

    df1 = pd.DataFrame([fix_id(x) for x in list(collection.find())])

    df2 = pd.DataFrame({
        "nome": ["Cliente X", "Cliente Y"],
        "email": ["x@gmail.com", "y@gmail.com"],
        "compras": [5, 8]
    })

    concatenado = pd.concat([df1, df2], ignore_index=True)

    st.write("Resultado da Concatenação:")
    st.dataframe(concatenado)

# CONSULTAR

elif menu == "Consultar Dados":
    st.subheader("Consulta de Dados")

    data = [fix_id(x) for x in list(collection.find())]

    if not data:
        st.info("Nenhum dado cadastrado.")
    else:
        df = pd.DataFrame(data)
        st.dataframe(df)