from flask import Flask, request, make_response

app = Flask(__name__)

"""
Maneja las solicitudes a la URL '/add/' y realiza una operación de suma.
Esta función toma dos números enteros directamente de la URL como parámetros 
'number1' y 'number2', los suma y retorna el resultado.

# Args:
number1 (int): El primer número entero a sumar, extraído de la URL.
number2 (int): El segundo número entero a sumar, extraído de la URL.

Returns:
str: Una cadena de texto que muestra la operación de suma y su resultado.
"""
@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"\n\n\t{number1} + {number2} = {number1 + number2}\n\n"

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
