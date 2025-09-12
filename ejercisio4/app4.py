from flask import Flask, request, make_response

app = Flask(__name__)

"""
Maneja las solicitudes a la URL '/hello' y responde según el método HTTP utilizado.
Si la solicitud es 'GET', retorna un mensaje indicando que se realizó una solicitud GET.
Si la solicitud es 'POST', retorna un mensaje indicando que se realizó una solicitud POST.
Si el método no es 'GET' o 'POST', retorna un mensaje de error.

Returns:
str: Una cadena de texto que indica el tipo de solicitud HTTP recibida.
"""
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return '\n\tYou made a GET request\n\n'
    elif request.method == 'POST':
        return '\n\tYou made a POST request\n\n'
    else:
        return 'You made an invalid request'

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
