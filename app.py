import streamlit as st
import pandas as pd

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
    for label in proyecciones["Mercado (Descripción)"].unique():
        subset = proyecciones[proyecciones["Mercado (Descripción)"] == label]
        st.line_chart(data=subset, x="Año", y="Valor (USD Millones)", use_container_width=True)
    st.dataframe(proyecciones)

elif seccion == "Crecimiento del Mercado":
    st.subheader("📊 Tasa de Crecimiento Proyectada")
    st.bar_chart(data=crecimiento, x="Periodo", y="Porcentaje (%)")
    st.dataframe(crecimiento)

elif seccion == "Participación Regional":
    st.subheader("🌎 Participación de Mercado por Región")
    st.dataframe(participacion)
    st.write("**Distribución de Participación:**")
    st.bar_chart(data=participacion.set_index("Región"))

elif seccion == "Competencia":
    st.subheader("🏗️ Empresas Competidoras en EE.UU.")
    st.dataframe(competencia)
    st.write("**Cantidad de competidores por estado:**")
    ubicaciones = competencia["Ubicación"].value_counts().reset_index()
    ubicaciones.columns = ["Ubicación", "Cantidad"]
    st.bar_chart(data=ubicaciones.set_index("Ubicación"))

elif seccion == "Cadenas Comerciales":
    st.subheader("🛒 Análisis de Cadenas Comerciales B2B")
    st.dataframe(cadenas)
    cadena_seleccionada = st.selectbox("Selecciona una cadena para ver sus ventajas", cadenas["Cadena Comercial"].unique())
    info = cadenas[cadenas["Cadena Comercial"] == cadena_seleccionada]
    st.markdown(f"**Descripción:** {info['Descripción'].values[0]}")
    st.markdown(f"**Ventajas para Eco 3D Innovations:** {info['Ventajas Clave'].values[0]}")
