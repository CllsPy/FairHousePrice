import pickle
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Estimativa de Preço", layout="centered")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Estimativa de Preço do Imóvel")

col1, col2 = st.columns(2)

with col1:
    area_m2 = st.number_input("Área (m²)", min_value=0.0, step=1.0)
    num_quartos = st.number_input("Quartos", min_value=0, step=1)

with col2:
    num_banheiros = st.number_input("Banheiros", min_value=0, step=1)
    idade_anos = st.number_input("Idade do imóvel (anos)", min_value=0, step=1)

if st.button("Calcular"):
    pred = model.predict([[area_m2, num_quartos, num_banheiros, idade_anos]])[0]
    st.metric("Preço estimado", f"{pred:,.2f}")


st.title("Dataset Usado")
data = pd.read_csv("house.csv")
st.write(data)