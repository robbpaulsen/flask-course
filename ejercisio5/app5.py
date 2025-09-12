from flask import Flask, request, make_response

app = Flask(__name__)

"""
Maneja las solicitudes a la URL '/greet/' y utiliza un parámetro dinámico.
La función toma una parte de la URL como un parámetro llamado 'name' y la usa para saludar al usuario.

Args:
name (str): El nombre proporcionado en la URL.

Returns:
str: Una cadena de texto que contiene un saludo personalizado.
"""
@app.route('/greet/<name>')
def greet(name):
    return f"\n\n\tHello {name}!\n\n"

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
