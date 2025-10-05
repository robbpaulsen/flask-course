"""
This script defines and configures a Flask web application with a basic login route and a file upload route.

---
### **`index()` function**

Handles the main route ('/') of the web application, managing both `GET` and `POST` requests.

-   `GET` requests render the `index.html` template.
-   `POST` requests process a login form, checking for a hardcoded username and password (`omar` and `password`).

---
### **`file_upload()` function**

Handles the `/file_upload` route, confirming the successful upload of a file.

---
### **Server Initialization**

Initializes the Flask development server. This code block ensures that the server runs only when the script is executed directly.

**Args:**
* `host` (str): The server's IP address. `'0.0.0.0'` makes the server accessible from external networks.
* `port` (int): The port on which the server listens for incoming requests.
* `debug` (bool): Enables debug mode, which automatically reloads the server on code changes and provides an interactive debugger 
in the browser for errors.

A continuación se muestra el comentario de código para la función `file_upload`.

Maneja la subida de archivos en la ruta '/file_upload'.
Procesa el contenido del archivo dependiendo de su tipo de contenido.
Si es un archivo de texto, devuelve su contenido como una cadena.
Si es un archivo de Excel, lo lee en un DataFrame de pandas y lo convierte a una tabla HTML para su visualización.

def file_upload():

### **Análisis de la Función**

  * **Propósito**: La función `file_upload()` está diseñada para gestionar la subida de archivos. Su lógica se basa en el tipo de contenido del archivo para determinar cómo procesarlo.

  * **Parámetros**: No recibe parámetros directamente, sino que accede a los datos del archivo subido a través del objeto `request.files` proporcionado por Flask.

  * **Retorno**: Dependiendo del tipo de archivo, la función puede retornar:

      * Una cadena de texto (`str`) con el contenido del archivo si es un archivo de texto plano.
      * Una cadena de texto con una tabla HTML (`str`) si es un archivo de Excel.
"""
import pandas as pd
from flask import Flask, render_template, request, Response


app = Flask(__name__, template_folder='templates')


@app.route(rule="/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')


        if username == 'omar' and password == 'password':
            return 'Welcome'
        else:
            return 'Failed Login Attempt'


@app.route(rule='/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']


    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )

    return  response

"""
Inicia el servidor de desarrollo de la aplicación web Flask.
Este bloque de código asegura que el servidor solo se ejecute 
cuando el script es ejecutado directamente.

Args:
- host (str): La dirección IP del host del servidor. '0.0.0.0' hace 
que el servidor esté accesible externamente.
- port (int): El puerto en el que el servidor escuchará las solicitudes entrantes.
- debug (bool): Habilita el modo de depuración, que recarga el servidor automáticamente 
al detectar cambios en el código y muestra un depurador interactivo en el
navegador en caso de errores.
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)