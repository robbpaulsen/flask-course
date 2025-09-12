from flask import Flask, request, make_response

app = Flask(__name__)


"""
# Esta función de vista maneja las solicitudes a la ruta '/hello'.
# Cuando se accede a esta URL, la función devuelve la cadena 'Hello From hello' como respuesta HTTP.

def hello_world():
    # No tiene parámetros de entrada.
    # Returns:
    #     str: La cadena de texto 'Hello From hello'.
"""
@app.route('/hello')
def hello_world():
    return 'Hello From hello'

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
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555, debug=True)
