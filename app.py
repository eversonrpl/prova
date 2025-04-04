import streamlit as st

st.title("Cálculo de Aumento Salarial")

nome = st.text_input("Qual é o seu nome e sobrenome:")
data_nascimento = st.number_input("Data de nascimento (apenas o ano):", min_value=1900, max_value=2100, step=1)
civil = st.selectbox("Estado civil:", ["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"])
sexo = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"])
salario = st.number_input("Salário:", min_value=0.0, step=0.01)

   
