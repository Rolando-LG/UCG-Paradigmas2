import streamlit as st
import libreria_funciones as lf

st.title("Paradigmas de la Programacion")
st.sidebar.image("UCG.png")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Rolando Lozado")

capital = st.number_input("Ingrese el capital")
tasa_anual_pct = st.number_input("Ingrese la tasa anual")
dias_mora = st.number_input("Ingrese los dias de mora")

resultado = lf.calcular_interes_mora(capital,tasa_anual_pct,dias_mora)

st.write("El Resultado por atraso de mora es: ")
