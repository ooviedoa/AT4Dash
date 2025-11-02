import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Carga de datos
df = pd.read_excel("NoFetal2019_BD.xlsx")

# Normalizamos los nombres de columnas para evitar errores
df.columns = df.columns.str.upper().str.strip()

# Detectamos columnas posibles
col_causa = next((c for c in df.columns if "COD_MUERTE" in c), None)
col_des_causa = next((c for c in df.columns if "MUERTE" in c), None)
col_muni = next((c for c in df.columns if "MUNICIPIO" in c or "CIUDAD" in c), None)
col_mes = next((c for c in df.columns if "MES" in c), None)
col_ano = next((c for c in df.columns if "ANO" in c or "AÑO" in c), None)
col_sexo = next((c for c in df.columns if "SEXO" in c), None)
col_depto = next((c for c in df.columns if "NOM_DEPARTAMENTO" in c ), None)


# Validación
if not all([col_causa, col_muni, col_mes, col_ano]):
    raise ValueError(f"⚠️ No se encontraron las columnas esperadas. "
                     f"Detectadas: causa={col_causa}, municipio={col_muni}, mes={col_mes}, año={col_ano}")


# ====================================================
# 1. Mapa de Muertes por departamento
# ====================================================

# Agrupar total de muertes por departamento y coordenadas
muertes_depto = (
    df.groupby(["NOM_DEPARTAMENTO", "LATITUD", "LONGITUD"])
    .size()
    .reset_index(name="TOTAL_MUERTES")
)

# === CREAR MAPA INTERACTIVO ===
fig_mapa = px.scatter_map(
    muertes_depto,
    lat="LATITUD",
    lon="LONGITUD",
    size="TOTAL_MUERTES",
    color="TOTAL_MUERTES",
    color_continuous_scale="Reds",
    size_max=45,
    zoom=4.5,
    hover_name="NOM_DEPARTAMENTO",
    hover_data={"LATITUD": False, "LONGITUD": False, "TOTAL_MUERTES": True},
    title="Distribución total de muertes por departamento en Colombia (2019)"
)

fig_mapa.update_layout(
    mapbox_style="open-street-map",  # estilo gratuito
    height=700,
    margin=dict(l=10, r=10, t=50, b=10),
    coloraxis_colorbar=dict(title="Total de muertes")
)

# ====================================================
# 2. GRÁFICO DE BARRAS – CIUDADES MÁS VIOLENTAS
# ====================================================

# Filtramos homicidios (Códigos X95, agresión con disparo de arma de fuego y casos no especificados)
df_hom = df[df[col_causa].astype(str).str.startswith("X95", na=False)]


# Agrupamos por municipio
ciudades_violentas = (
    df_hom.groupby("MUNICIPIO")
    .size()
    .reset_index(name="Total_homicidios")
    .sort_values("Total_homicidios", ascending=False)
    .head(5)
)

#print(df_hom[col_muni])

# Creamos gráfico de barras
fig_barras = px.bar(
    ciudades_violentas,
    x="MUNICIPIO",
    y="Total_homicidios",
    #title="5 ciudades más violentas de Colombia (Homicidios - Códigos X95)",
    text="Total_homicidios",
    color="Total_homicidios",
    color_continuous_scale="Reds"
)

fig_barras.update_traces(textposition="outside")
fig_barras.update_layout(
    xaxis_title="Ciudad / Municipio",
    yaxis_title="Total de homicidios",
    uniformtext_minsize=8,
    uniformtext_mode="hide"
)

# ====================================================
# 3. GRÁFICO DE LÍNEAS – MUERTES POR MES
# ====================================================
df_mes = df.groupby(col_mes).size().reset_index(name="Total_muertes")
df_mes = df_mes.sort_values(col_mes)

# Crear nombre del mes (en texto)
df_mes["Mes_nombre"] = df_mes[col_mes].apply(
    lambda m: pd.to_datetime(str(m), format="%m").strftime("%B")
)

fig_lineas = px.line(
    df_mes,
    x="Mes_nombre",
    y="Total_muertes",
    markers=True,
    #title="Muertes por mes en Colombia (2019)"
)
fig_lineas.update_layout(xaxis_title="Mes", yaxis_title="Total de muertes")

# ====================================================
# 4. GRÁFICO CIRCULAR – 10 CIUDADES CON MENOR MORTALIDAD
# ====================================================
ciudades_menor_mortalidad = (
    df.groupby("MUNICIPIO")
    .size()
    .reset_index(name="Total_muertes")
    .sort_values("Total_muertes", ascending=True)
    .head(10)
)

fig_pie = px.pie(
    ciudades_menor_mortalidad,
    names="MUNICIPIO",
    values="Total_muertes",
    #title="10 ciudades con menor índice de mortalidad (2019)",
    hole=0.3  # gráfico tipo 'donut' para mejor visualización
)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')

# ====================================================
# 5. TABLA – 10 PRINCIPALES CAUSAS DE MUERTE
# ====================================================

# Agrupamos las causas más comunes
causas_principales = (
    df.groupby(["COD_MUERTE","MUERTE"])
    .size()
    .reset_index(name="Total_muertes")
    .sort_values("Total_muertes", ascending=False)
    .head(10)
)

# Renombrar columna para la tabla
causas_principales.rename(columns={
    "MUERTE": "Descripción",
    "COD_MUERTE": "Código"
}, inplace=True)

# Agregar un código genérico (si no tienes una columna de código)
#causas_principales.rename(columns={col_causa: "Código"}, inplace=True)

#print(causas_principales["COD_MUERTE"])

# Crear tabla en Dash
tabla_causas = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in causas_principales.columns],
    data=causas_principales.to_dict("records"),
    style_header={
        "backgroundColor": "#004c70",
        "color": "white",
        "fontWeight": "bold",
        "textAlign": "center"
    },
    style_cell={
        "textAlign": "left",
        "padding": "8px",
        "whiteSpace": "normal",
        "height": "auto"
    },
    style_table={"marginTop": "20px", "width": "80%", "margin": "auto"},
    style_data_conditional=[
        {"if": {"row_index": "odd"}, "backgroundColor": "#f2f2f2"},
        {"if": {"row_index": "even"}, "backgroundColor": "#ffffff"},
    ],
    page_size=10,
)

# ====================================================
# 6. GRÁFICO DE BARRAS APILADAS – MUERTES POR SEXO Y DEPARTAMENTO
# ====================================================

# Mapear valores numéricos a etiquetas de texto
map_sexo = {1: "Masculino", 2: "Femenino", 3: "Indeterminado"}
df["Sexo_texto"] = df[col_sexo].map(map_sexo).fillna("Desconocido")

# Agrupamos por departamento y sexo
df_sexo_depto = (
    df.groupby([col_depto, "Sexo_texto"])
    .size()
    .reset_index(name="Total_muertes")
)

# Creamos el gráfico de barras apiladas
fig_barras_apiladas = px.bar(
    df_sexo_depto,
    x=col_depto,
    y="Total_muertes",
    color="Sexo_texto",
    #title="Comparación del total de muertes por sexo en cada departamento (2019)",
    labels={col_depto: "Departamento", "Total_muertes": "Total de muertes", "Sexo_texto": "Sexo"},
    height=700
)

fig_barras_apiladas.update_layout(
    barmode="stack",
    xaxis_tickangle=-45,
    xaxis_title="Departamento",
    yaxis_title="Total de muertes",
    legend_title="Sexo",
    title_x=0.5
)

# ====================================================
# 7. HISTORIGRAMA
# ====================================================

# Mapeo de GRUPO_EDAD1 a categorías descriptivas (según tabla DANE)
map_grupo = {
    (0, 4): "Mortalidad neonatal",
    (5, 6): "Mortalidad infantil",
    (7, 8): "Primera infancia",
    (9, 10): "Niñez",
    (11, 11): "Adolescencia",
    (12, 13): "Juventud",
    (14, 16): "Adultez temprana",
    (17, 19): "Adultez intermedia",
    (20, 24): "Vejez",
    (25, 28): "Longevidad / Centenarios",
    (29, 29): "Edad desconocida"
}

# Función para asignar categoría según GRUPO_EDAD1
def clasificar_grupo(codigo):
    try:
        codigo = int(codigo)
        for rango, nombre in map_grupo.items():
            if rango[0] <= codigo <= rango[1]:
                return nombre
        return "No especificado"
    except:
        return "No especificado"

# Crear nueva columna categórica
df["Grupo_edad_categoria"] = df["GRUPO_EDAD1"].apply(clasificar_grupo)

# Contar muertes por grupo de edad
df_hist = (
    df.groupby("Grupo_edad_categoria")
    .size()
    .reset_index(name="Total_muertes")
    .sort_values("Total_muertes", ascending=False)
)

# Crear histograma
fig_hist = px.bar(
    df_hist,
    x="Grupo_edad_categoria",
    y="Total_muertes",
    #title="Distribución de muertes por grupo de edad (Colombia, 2019)",
    labels={"Grupo_edad_categoria": "Grupo de edad", "Total_muertes": "Total de muertes"},
    color="Grupo_edad_categoria",
    height=700
)

fig_hist.update_layout(
    xaxis_tickangle=-45,
    showlegend=False
)

# ====================================================
# 8. INTERFAZ DASH
# ====================================================
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Mortalidad en Colombia - 2019", style={"textAlign": "center"}),

    html.Div(
        dcc.Graph(figure=fig_mapa,
            config={
                "scrollZoom": True,     # ✅ permite zoom con el scroll del mouse
                "displayModeBar": True, # ✅ muestra barra de herramientas
                "displaylogo": False,   # quita logo de Plotly
                "modeBarButtonsToAdd": [
                    "zoomInMapbox",
                    "zoomOutMapbox",
                    "resetViewMapbox"
                ],
            }),
        style={"width": "95%", "margin": "auto"}
    ),

    html.H2("Gráfico de líneas: Total de muertes por mes", style={"marginTop": "40px", "textAlign": "center"}),
    dcc.Graph(figure=fig_lineas),

    html.H2("Gráfico de barras: 5 ciudades más violentas", style={"marginTop": "40px", "textAlign": "center"}),
    dcc.Graph(figure=fig_barras),

    html.H2("Gráfico circular: 10 ciudades con menor mortalidad", style={"marginTop": "40px", "textAlign": "center"}),
    dcc.Graph(figure=fig_pie),

    html.H2("Tabla: 10 principales causas de muerte en Colombia", style={"marginTop": "40px", "textAlign": "center"}),
    tabla_causas,

    html.H2("Gráfico de barras apiladas: Total de muertes por sexo y departamento", style={"marginTop": "40px", "textAlign": "center"}),
    dcc.Graph(figure=fig_barras_apiladas),

    html.H2("Distribución por Edad", style={"marginTop": "40px", "textAlign": "center"}),
    dcc.Graph(figure=fig_hist),

])

server = app.server

# ====================================================
# 5. EJECUCIÓN DEL SERVIDOR
# ====================================================
if __name__ == "__main__":

    app.run(debug=True)

