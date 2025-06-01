import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título del dashboard
st.title("📊 Dashboard Dinámico - Eco3D Innovations")

# Cargar archivos desde GitHub (actualiza las URLs con tus rutas reales en GitHub)
@st.cache_data
def load_data():
    proyecciones = pd.read_csv("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/proyecciones.csv")
    crecimiento = pd.read_csv("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/crecimiento.csv")
    participacion = pd.read_csv("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/participacion.csv")
    competencia = pd.read_csv("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/competencia.csv")
    cadenas = pd.read_csv("https://raw.githubusercontent.com/tu_usuario/tu_repo/main/cadenas_comerciales.csv")
    return proyecciones, crecimiento, participacion, competencia, cadenas

proyecciones, crecimiento, participacion, competencia, cadenas = load_data()

# Sidebar para seleccionar sección
seccion = st.sidebar.radio("Selecciona la sección", [
    "Proyecciones de Mercado",
    "Crecimiento del Mercado",
    "Participación Regional",
    "Competencia",
    "Cadenas Comerciales"
])

# Visualizaciones por sección
if seccion == "Proyecciones de Mercado":
    st.subheader("📈 Proyecciones del Mercado de Impresión 3D")
    fig, ax = plt.subplots()
    for label in proyecciones["Mercado (Descripción)"].unique():
        subset = proyecciones[proyecciones["Mercado (Descripción)"] == label]
        ax.plot(subset["Año"], subset["Valor (USD Millones)"], marker='o', label=label)
    ax.set_xlabel("Año")
    ax.set_ylabel("Millones USD")
    ax.set_title("Proyecciones del mercado")
    ax.legend()
    st.pyplot(fig)
    st.dataframe(proyecciones)

elif seccion == "Crecimiento del Mercado":
    st.subheader("📊 Tasa de Crecimiento Proyectada")
    fig, ax = plt.subplots()
    ax.bar(crecimiento["Periodo"], crecimiento["Porcentaje (%)"], color="skyblue")
    ax.set_ylabel("Crecimiento Anual (%)")
    ax.set_title("Crecimiento del Mercado")
    st.pyplot(fig)
    st.dataframe(crecimiento)

elif seccion == "Participación Regional":
    st.subheader("🌎 Participación de Mercado por Región")
    fig, ax = plt.subplots()
    ax.pie(participacion["Participación de mercado (%)"], labels=participacion["Región"], autopct='%1.1f%%')
    ax.set_title("Distribución Regional del Mercado 3D")
    st.pyplot(fig)
    st.dataframe(participacion)

elif seccion == "Competencia":
    st.subheader("🏗️ Empresas Competidoras en EE.UU.")
    st.dataframe(competencia)
    st.write("**Cantidad de competidores por estado:**")
    fig, ax = plt.subplots()
    competencia["Ubicación"].value_counts().plot(kind="bar", ax=ax, color="lightgreen")
    ax.set_ylabel("Cantidad de empresas")
    ax.set_xlabel("Ubicación")
    ax.set_title("Distribución de competidores por ubicación")
    st.pyplot(fig)

elif seccion == "Cadenas Comerciales":
    st.subheader("🛒 Análisis de Cadenas Comerciales B2B")
    st.dataframe(cadenas)
    cadena_seleccionada = st.selectbox("Selecciona una cadena para ver sus ventajas", cadenas["Cadena Comercial"].unique())
    info = cadenas[cadenas["Cadena Comercial"] == cadena_seleccionada]
    st.markdown(f"**Descripción:** {info['Descripción'].values[0]}")
    st.markdown(f"**Ventajas para Eco 3D Innovations:** {info['Ventajas Clave'].values[0]}")

