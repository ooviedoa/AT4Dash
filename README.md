# AT4Dash
Actividad 4 Aplicaciones Despliegue Dash

## Introducción del proyecto

En este proyecto se muestran diferentes gráficos sobre la mortalidad de Colombia en el año 2019, para esto usamos las bibliotecas de plotly, pandas y dash para mostrar la información y subir el proyecto a un servidos PaaS. La información fue descargada desde la página oficial del Departamento Administrativo Nacional de Estadísticas (DANE) de Colombia.

# Objetivo

El proyecto busca mostrar estadísticamente las causas, la orientación sexual, la ubicación y las edades de la mortalidad de los colombianos mediante el uso de diferentes gráficos interactivos.

# Estructura del proyecto

📁Carpeta principal:
  |- README.md: Contiene la descripción del proyecto
  |- NoFetal2019_BD.xlsx: Contiene la información de la mortalidad de Colombia en 2019
  |- requeriments.txt: Contiene las librerias del proyecto
  |- 📁Carpeta src:
       |- app.py: Código principal del proyecto

# Requisitos: 

🧰 Las librerias necesarias para el proyecto son:

dash==3.2.0
dash-bootstrap-components==2.0.4
dash-table==5.0.0
gunicorn==23.0.0
plotly==6.3.1
pandas==2.3.3
openpyxl==3.1.5

# Despliegue en Render
Para desplegar estas aplicaciones en Render, se recomienda seguir la siguiente estructura y archivos clave: 

• src/: Carpeta que contiene el código fuente de la aplicación. o app.py: Archivo principal donde se instancia la aplicación Dash. Dentro de este archivo, la instrucción server = app.server expone el servidor Flask subyacente, requisito indispensable para que Render pueda ejecutar la aplicación correctamente. 

• render.yaml: Archivo de configuración específico para Render. Define aspectos como: o El entorno de ejecución (por ejemplo, Python 3.11), o Comando para iniciar la aplicación (como gunicorn src.app:server), o Variables de entorno necesarias para el entorno de producción. 

• requirements.txt: Archivo que lista todas las dependencias del proyecto, incluyendo Dash, Flask y cualquier otra librería utilizada. Render lo usa para instalar automáticamente los paquetes requeridos. 

• README.md: Documento descriptivo que sirve como guía técnica del proyecto. Incluye: o Resumen del propósito de la aplicación, o Instrucciones para ejecución local, o Detalles sobre el despliegue en Render. 

### Crear un proyecto Dash: 

• Empieza creando tu aplicación Dash en tu máquina local y asegúrate de que tenga una estructura adecuada. Crea un archivo principal llamado app.py, donde se define tu aplicación Dash como se muestra a continuación 

### Crea el archivo requirements.txt: 

• Asegúrate de tener un archivo requirements.txt en tu proyecto. Este archivo debe incluir todas las dependencias necesarias para que Render instale automáticamente los paquetes al desplegar la aplicación (por ejemplo, Dash y otras librerías necesarias).  Nota: gunicorn es obligatorio para ejecutar la aplicación en un servidor de producción.

### Subir el Proyecto a GitHub

Render se integra directamente con plataformas como GitHub o GitLab, por lo que es necesario tener el código fuente alojado en un repositorio, ya sea público o privado. Pasos para subir el proyecto a GitHub: 1. Crea un nuevo repositorio en tu cuenta de GitHub  2. Desde tu terminal, inicializa el repositorio local y sube los archivos: Nota: Si no deseas usar la terminal, también puedes crear directamente la estructura del proyecto desde la interfaz web de GitHub, agregando carpetas y archivos manualmente (como el README.md, requirements.txt, etc.), y luego conectarlo con Render para el despliegue. UNIDAD 2: 59 Aplicaciones web analíticas con Python y Dash 

### Crear un nuevo Servicio en Render 

1. Ve a Render y crea una cuenta si no tienes una.

2. En el dashboard, haz clic en New  → Web Service.
  
3. Conéctalo con el repositorio de GitHub donde subiste tu código. 
  
4. Configura los siguientes parámetros: o Runtime: Python 3.x o Start Command: gunicorn app:server o Environment: Auto-detect

### Desplegar y Probar la Aplicación  

Una vez tengas tu aplicación desarrollada y alojada en el repositorio de GitHub, puedes desplegarla en Render.

Despliegue Manual desde la Web de Render 

1. Importante: asegúrate de que tu archivo src/app.py tenga esta línea: server = app.server
 
2. Ve a https://render.com y selecciona New → Web Service.
  
3. Conecta tu cuenta de GitHub y selecciona el repositorio que contiene tu aplicación Dash.
   
4. Completa los campos del formulario: • Name: Escribe un nombre para tu servicio (por ejemplo: proyecto-dash). • Root Directory: Déjalo vacío si el archivo app.py está dentro de la carpeta src/. • Environment: Selecciona Python 3. • Build Command: pip install -r requirements.txt • Start Command: gunicorn src.app:server

5. Selecciona el tipo de instancia: Marca la opción Free (gratuita), que incluye 512 Mb (RAM) y 1 CPU al mes (suficiente para pruebas o proyectos educativos).

6. (Opcional) Si necesitas variables de entorno (por ejemplo, tokens o claves), agrégalas en la sección Environment Variables.

7. Haz clic en “Create Web Service” o “Deploy Web Service” al final del formulario.

8. Espera unos minutos mientras Render instala las dependencias y despliega la app.

9. Una vez finalizado, Render mostrará una URL pública como: https://proyecto.onrender.com 

## Software

El software utilizado fue: Visual studio code, python, Dash

## Instalación

Instalación local

### Clona el repositorio:

git clone https://github.com/usuario/AT4Dash.git
cd AT4Dash


### Crea un entorno virtual (opcional):

python -m venv venv
source venv/Scripts/activate   # En Windows
source venv/bin/activate       # En Linux/Mac


### Instala las dependencias:

pip install -r requirements.txt


### Ejecuta la aplicación:

python main.py


### Abre tu navegador en:

http://127.0.0.1:8050

## Visualizaciones de los resultados:

<img width="1817" height="862" alt="image" src="https://github.com/user-attachments/assets/1c162689-a462-45f5-9c3f-c4bf37f60d21" />

<img width="1853" height="497" alt="image" src="https://github.com/user-attachments/assets/4d7a65e6-878f-4598-a252-18a811bd6e4c" />

<img width="1874" height="492" alt="image" src="https://github.com/user-attachments/assets/a92514c6-2631-4043-87ba-e941487f6466" />

<img width="1314" height="514" alt="image" src="https://github.com/user-attachments/assets/eef9372a-410d-4ea2-a258-c95556f20b0c" />

<img width="1635" height="483" alt="image" src="https://github.com/user-attachments/assets/48621b0f-5c9c-4004-b07e-85ff41151b9f" />

<img width="1887" height="554" alt="image" src="https://github.com/user-attachments/assets/db4ec232-5b39-43f8-a55f-c2ae61c8bee5" />

<img width="1890" height="746" alt="image" src="https://github.com/user-attachments/assets/8b9c63c4-00a8-4d68-9343-76a3b3dfe1d7" />







