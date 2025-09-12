from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


"""
Initializes and runs a Flask web application.

This script sets up a basic Flask application, defining a single route for the 
root URL ('/'). When a user accesses this URL, the `index` function is called, 
which renders and returns the `index.html` template. The `if __name__ == "__main__":` 
block ensures the development server starts when the script is executed directly.```
"""
@app.route('/')
def index():
    myvalue = 'momentummindset'
    mylist = [1, 2, 3, 4, 5]
    # myresult = 10 + 30
    return render_template(template_name_or_list='index.html', mylist=mylist, myvalue=myvalue)


"""
# Esta función maneja las solicitudes a la ruta '/other' y renderiza la plantilla HTML 'other.html'.
Renderiza la página 'other'.
    Returns:
        str: El contenido HTML de la plantilla 'other.html'.
"""
@app.route('/other')
def other():
    return render_template(template_name_or_list='other.html')


"""
Esta función maneja las solicitudes a la ruta '/filters', define una variable llamada 
'some_text' con el valor 'Hello World!' y luego renderiza la plantilla HTML 'filters.html', 
pasando la variable 'some_text' a la plantilla para que pueda ser utilizada.
    
    Renderiza la página 'filters' y pasa una cadena de texto a la plantilla.
    Returns:
        str: El contenido HTML de la plantilla 'filters.html'.
"""
@app.route('/filters')
def filters():
    some_text = 'Hello World!'
    return render_template(template_name_or_list='filters.html', some_text=some_text)


"""
Esta función es un filtro de plantilla personalizado de Jinja2.
Su propósito es revertir una cadena de texto. Se registra como un filtro
llamado 'reverse_string' para poder ser utilizado dentro de las plantillas de Jinja2.

    Invierte una cadena de texto.
    Args:
        s (str): La cadena de texto que se va a invertir.

    Returns:
        str: La cadena de texto invertida.
"""
@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1] # This is a Python slice that reverses a string


"""
La función `repeat` es otro filtro que repite una cadena de texto un número de veces, 
con un valor predeterminado de 2
"""
@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

"""
la función `alternate_case` es un filtro que toma una cadena de texto y
convierte cada carácter a mayúscula o minúscula de forma alternada.
Utiliza una comprensión de lista para iterar sobre la cadena,
convirtiendo los caracteres en posiciones pares (0, 2, 4...) a mayúsculas
y los caracteres en posiciones impares (1, 3, 5...) a minúsculas.

El bloque de plantilla HTML `content` demuestra cómo aplicar este filtro
a la variable `some_text` para mostrar el texto con el formato de mayúsculas
y minúsculas alternado.
"""
@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate (s)])

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
