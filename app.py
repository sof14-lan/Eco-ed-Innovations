print("✅ Archivo app.py correcto está corriendo")
import dash
from dash import dcc, html
import dash_table
import pandas as pd
import plotly.express as px

# =====================
# Carga de datos
# =====================

df_crecimiento = pd.read_excel("data/Crecimiento.xlsx", sheet_name="Crecimiento")
df_participacion = pd.read_excel("data/participación.xlsx", sheet_name="participación")
df_proyecciones = pd.read_excel("data/proyecciones.xlsx", sheet_name="Hoja1")
df_competencia = pd.read_excel("data/Competencia.xlsx", sheet_name="Competencia ")
df_cadenas = pd.read_excel("data/cadenas comerciales.xlsx", sheet_name="Hoja1")

# =====================
# Inicialización de la app
# =====================
app = dash.Dash(_name_)
app.title = "Dashboard de Cadenas Comerciales"

# =====================
# Layout del Dashboard
# =====================
app.layout = html.Div([
    html.H1("Dashboard de Cadenas Comerciales", style={"textAlign": "center", "marginBottom": "30px"}),

    html.H2("Proyecciones de Ventas"),
    dcc.Graph(
        figure=px.line(df_proyecciones, 
                       x=df_proyecciones.columns[0], 
                       y=df_proyecciones.columns[1:], 
                       markers=True, 
                       title="Proyecciones por Cadena")
    ),

    html.H2("Participación de Mercado"),
    dcc.Graph(
        figure=px.bar(df_participacion, 
                      x=df_participacion.columns[0], 
                      y=df_participacion.columns[1:], 
                      barmode="group", 
                      title="Participación por Año")
    ),

    html.H2("Crecimiento Anual"),
    dcc.Graph(
        figure=px.line(df_crecimiento, 
                       x=df_crecimiento.columns[0], 
                       y=df_crecimiento.columns[1:], 
                       markers=True, 
                       title="Crecimiento de las Cadenas")
    ),

    html.H2("Competencia"),
    dash_table.DataTable(
        data=df_competencia.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df_competencia.columns],
        style_table={'overflowX': 'auto', 'marginBottom': '40px'},
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
    ),

    html.H2("Información Cualitativa de Cadenas"),
    dash_table.DataTable(
        data=df_cadenas.iloc[1:].to_dict('records'),
        columns=[
            {"name": "Cadena Comercial", "id": df_cadenas.columns[1]},
            {"name": "Descripción", "id": df_cadenas.columns[2]},
            {"name": "Ventajas Clave", "id": df_cadenas.columns[3]},
        ],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
    )
])

# =====================
# Ejecutar Servidor
# =====================
if _name_ == "_main_":
    app.run_server(debug=True)
