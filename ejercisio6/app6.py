from flask import Flask, request, make_response

app = Flask(__name__)

"""
Maneja las solicitudes a la URL '/status' y retorna un mensaje con un código de estado HTTP específico.
La función retorna un mensaje de texto "Hello World" junto con el código de estado HTTP 404 (Not Found).

Returns:
tuple: Una tupla que contiene una cadena de texto y un código de estado HTTP.
"""
@app.route('/status')
def status():
    return ('\n\n\tHello World\n\n', 404)

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
