# AT4Dash
Actividad 4 Aplicaciones Despliegue Dash

## Introducción del proyecto

En este proyecto se muestran diferentes gráficos sobre la mortalidad de Colombia en el año 2019, para esto usamos las bibliotecas de plotly, pandas y dash para mostrar la información y subir el proyecto a un servidos PaaS. La información fue descargada desde la página oficial del Departamento Administrativo Nacional de Estadísticas (DANE) de Colombia.

# Objetivo

El proyecto busca mostrar estadísticamente las causas, la orientación sexual, la ubicación y las edades de la mortalidad de los colombianos mediante el uso de diferentes gráficos interactivos.

# Estructura del proyecto

Carpeta principal:
│
├──
  |- README.md # Contiene la descripción del proyecto
  |- NoFetal2019_BD.xlsx: Contiene la información de la mortalidad de Colombia en 2019
  |- requeriments.txt: Contiene las librerias del proyecto
  |- Carpeta src:
       |- app.py: Código principal del proyecto

# Requisitos: 

Las librerias necesarisas para el proyecto son:

dash==3.2.0
dash-bootstrap-components==2.0.4
dash-table==5.0.0
gunicorn==23.0.0
plotly==6.3.1
pandas==2.3.3
openpyxl==3.1.5



