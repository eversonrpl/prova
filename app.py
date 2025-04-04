import streamlit as st

def main():
    st.title("Cálculo de Aumento Salarial")

    nome = st.text_input("Qual é o seu nome e sobrenome:")
    data_nascimento = st.number_input("Data de nascimento (apenas o ano):", min_value=1900, max_value=2100, step=1)
    civil = st.selectbox("Estado civil:", ["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"])
    sexo = st.selectbox("Sexo:", ["Masculino", "Feminino", "Outro"])
    salario = st.number_input("Salário:", min_value=0.0, step=0.01)

    if st.button("Calcular Aumento"):
        st.write(f"O funcionário de nome {nome}, nascido em {data_nascimento}, de estado civil {civil} e do sexo {sexo}, recebe o salário de R$ {salario:.2f}.")

        if salario > 2500.00:
            aumento = 500
            salario += aumento
            st.write(f"Funcionário deve receber aumento. Seu novo salário será R$ {salario:.2f}.")
        else:
            st.write("Funcionário não deve receber aumento.")

if __name__ == "__main__":
    main()


   
