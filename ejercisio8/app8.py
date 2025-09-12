from flask import Flask, request, make_response

app = Flask(__name__)

"""
Maneja las solicitudes a la URL '/handle_url_params' y extrae parámetros de la 
cadena de consulta (query string). La función busca los parámetros 'greeting' y 
'name' en la URL. Si ambos están presentes, retorna una cadena con el saludo y el nombre.
De lo contrario, retorna un mensaje indicando que los parámetros no fueron encontrados.

Returns:
str: Una cadena de texto que contiene el saludo y el nombre, o un mensaje de
error si los parámetros no están presentes.
"""
@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'No greeting or name parameter found'

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
