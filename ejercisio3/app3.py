from flask import Flask, request, make_response

app = Flask(__name__)


"""
Crea una respuesta HTTP que contiene el cuerpo 'Hello World', establece el código de estado en 
202 (Accepted) y configura el encabezado 'Content-Type' como 'application/octet-stream'.
Este código es útil para indicar que la solicitud ha sido recibida y aceptada para procesamiento, 
pero la acción aún no se ha completado.

```bash
curl -I http://127.0.0.1:5000/response

HTTP/1.1 202 ACCEPTED
Server: Werkzeug/3.1.3 Python/3.11.13
Date: Fri, 05 Sep 2025 22:40:56 GMT
Content-Type: application/octet-stream
Content-Length: 11
Connection: close
```
"""
@app.route('/response')
def response():
    response = make_response('Hello World')
    response.status_code = 202
    response.headers['Content-Type'] = 'application/octet-stream'
    return response

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
