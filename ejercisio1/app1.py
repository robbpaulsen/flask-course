from flask import Flask, request, make_response

app = Flask(__name__)

"""
### ¿Qué es Flask?

Flask es un **micro-framework web** para Python. Esto significa que es una herramienta simple 
y ligera que te ayuda a construir aplicaciones web, como páginas, APIs o servicios. A 
diferencia de otros frameworks más grandes, Flask no viene con muchas funciones preinstaladas; te 
da la libertad de elegir los componentes que necesites para tu proyecto.

### Casos de uso

Flask es ideal para:

* **APIs y servicios web:** Es muy usado para crear APIs RESTful de manera rápida y sencilla.
* **Proyectos pequeños y medianos:** Como blogs, portafolios en línea o herramientas internas de una empresa.
* **Prototipos:** Es perfecto para probar ideas y construir un MVP (Producto Mínimo Viable) en poco tiempo.
* **Aplicaciones de una sola página (SPA):** Se puede usar como backend para una aplicación frontend hecha con JavaScript.

### Problemáticas que resuelve

Flask resuelve el problema de tener que empezar desde cero para cada proyecto web. Te proporciona 
una estructura básica para manejar cosas comunes como:

* **Enrutamiento (routing):** Relaciona URLs con funciones de Python.
* **Manejo de peticiones:** Recibe y procesa la información que el usuario envía.
* **Plantillas (templates):** Permite generar HTML dinámico para las páginas web.

### ¿Por qué usar Flask ante otras propuestas?

La principal razón para elegir Flask es su **filosofía de ser simple y minimalista**. Mientras 
que otros frameworks como Django vienen con muchas herramientas (un ORM, un panel de administración, etc.), 
Flask te da solo lo esencial. Esto te permite:

* **Flexibilidad:** Tienes el control total sobre la arquitectura de tu proyecto y puedes 
elegir las librerías que mejor se adapten a tus necesidades.
* **Menos código "mágico":** El código de Flask es muy transparente y fácil de entender. No 
hay muchas cosas ocultas que hagan la depuración más difícil.

### Ventajas de Flask sobre otras propuestas

* **Ligero y rápido:** Al tener menos componentes, el framework es más pequeño y, por lo 
tanto, la curva de aprendizaje es más rápida.
* **Fácil de aprender:** Su sintaxis es sencilla, lo que lo hace ideal para principiantes.
* **Extensible:** Su filosofía "sin opiniones" te permite integrar cualquier librería de Python, 
lo que lo hace muy versátil.
* **Excelente documentación:** La documentación de Flask es muy clara y útil.

### ¿Cuándo es conveniente y cuándo no usar Flask?

#### **Es conveniente cuando:**

* Necesitas construir una aplicación web pequeña o mediana.
* Buscas total control sobre las librerías y componentes.
* Tu equipo ya está familiarizado con Python y quieres un framework que sea fácil 
de aprender y usar.
* Estás creando un API o un servicio web ligero.

#### **No es conveniente cuando:**

* Necesitas una aplicación muy grande y compleja, como una red social, que requiera 
muchas funciones predefinidas (manejo de usuarios, bases de datos, etc.). En estos casos, 
un framework más completo como **Django** te podría ahorrar mucho tiempo.
* Buscas una solución "llave en mano" que ya tenga integradas las herramientas comunes 
para proyectos grandes, como un sistema de autenticación de usuarios.
* El proyecto requiere un alto nivel de escalabilidad desde el inicio y un equipo de 
desarrolladores que prefiera una estructura más rígida y "con opiniones".
"""

"""
Flask permite generar rutas nuevas muy facilmente, cada ruta se especifica declarando primero
el nombre que se le asignara empezando desde la raiz de la url. que inicia en el 
http://127.0.0.1:5000/ <---- Ahi "/" .

El uso de 'return' y no de 'print' envía una respuesta al navegador del usuario, en una función de Flask 
que es asociada a una ruta, el valor que se devuelve se convierte en la respuesta HTTP que el servidor le 
envía al cliente (el navegador web). En este ejemplo, `return "<h1>Hello World</h1>"` hace que el navegador 
reciba ese código HTML y lo muestre como una página web.
"""
@app.route('/')
def index():
    return "<h1>Hello From Index</h1>"

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
