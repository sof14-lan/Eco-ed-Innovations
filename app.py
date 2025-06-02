import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga de archivos
@st.cache_data
def load_data():
    cadenas = pd.read_excel("cadenas_comerciales.xlsx", skiprows=1)
    competencia = pd.read_excel("Competencia.xlsx", skiprows=1)
    crecimiento = pd.read_excel("Crecimiento.xlsx", skiprows=1)
    participacion = pd.read_excel("participación.xlsx", skiprows=1)
    proyecciones = pd.read_excel("proyecciones.xlsx", skiprows=1)
    return cadenas, competencia, crecimiento, participacion, proyecciones

cadenas, competencia, crecimiento, participacion, proyecciones = load_data()

# Menú lateral
st.sidebar.title("Dashboard 3D Construction")
opcion = st.sidebar.radio("Selecciona una vista", [
    "Cadenas Comerciales", 
    "Competencia", 
    "Crecimiento del Mercado", 
    "Participación Regional", 
    "Proyecciones Globales"
])

# Cadenas Comerciales
if opcion == "Cadenas Comerciales":
    st.title("Cadenas Comerciales")
    st.dataframe(cadenas)

# Competencia
elif opcion == "Competencia":
    st.title("Competencia")
    st.dataframe(competencia)
    if st.checkbox("Ver empresas por país"):
        paises = competencia["Unnamed: 2"].unique()
        filtro = st.selectbox("Selecciona país", paises)
        st.dataframe(competencia[competencia["Unnamed: 2"] == filtro])

# Crecimiento del Mercado
elif opcion == "Crecimiento del Mercado":
    st.title("Crecimiento del Mercado")
    st.dataframe(crecimiento)
    fig, ax = plt.subplots()
    ax.bar(crecimiento["Unnamed: 1"], crecimiento["Unnamed: 3"])
    ax.set_ylabel("Crecimiento (%)")
    ax.set_title("Tasa de Crecimiento por Periodo")
    st.pyplot(fig)

# Participación Regional
elif opcion == "Participación Regional":
    st.title("Participación Regional de Mercado")
    st.dataframe(participacion)
    fig, ax = plt.subplots()
    ax.bar(participacion["Región"], participacion["Participación de mercado (%)"])
    ax.set_ylabel("% Participación")
    st.pyplot(fig)

# Proyecciones Globales
elif opcion == "Proyecciones Globales":
    st.title("Proyecciones del Mercado")
    st.dataframe(proyecciones)
    fig, ax = plt.subplots()
    ax.plot(proyecciones["Año"], proyecciones["Unnamed: 3"])
    ax.set_ylabel("Valor (USD Millones)")
    ax.set_title("Proyección de Tamaño de Mercado")
    st.pyplot(fig)
