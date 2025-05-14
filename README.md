# Creación de un modelo estimador de Trading

* Autor: Neobytes84
* Project_URL: https://github.com/neobytes84/api-flask

En el panorama web interconectado actual, la gestión eficiente de diferentes microservicios es crucial para cualquier aplicación web. Una puerta de enlace de API puede agilizar este proceso al actuar como un centro que dirige el tráfico y atiende las solicitudes de los clientes a varios servicios de backend. En este estudio de caso, exploraremos cómo crear una puerta de enlace API robusta utilizando Flask, un popular marco web de Python.

## Objetivos

  - Comprensión de los aspectos básicos de las puertas de enlace de API.
  - Configuración un entorno de Flask
  - Implementación de rutas y funcionalidades en Flask que actúen como puerta de enlace de API.
  - Manejar solicitudes y respuestas hacia y desde varios servicios.
  - Implementación la puerta de enlace de API y pruebe su funcionalidad.

## Descripción de las puertas de enlace de API

Una puerta de enlace de API actúa como un único punto de entrada para varios microservicios. Gestiona las solicitudes enrutándolas al servicio de backend adecuado, consolidando las respuestas y, a veces, transformándolas o agregándolas antes de enviarlas de vuelta al cliente.

Entre las ventajas de utilizar una puerta de enlace de API se incluyen:

  - Gestión centralizada de la autenticación y la autorización.
  - Balanceo de carga entre diferentes servicios.
  - Limitación de velocidad para evitar abusos.
  - Capacidades de monitoreo y análisis.

## Configuración del entorno

 Asegúrese de tener Python 3.12 instalado en su sistema o superior. Una vez instalado puede crear un entorno virtual e instalar Flask.
 
## Creación de carpeta, entorno virtual e instalación de Flask 
   - mkdir api-flask
   - cd api-flask
   - python -m venv ven
   - .\ven\Scripts\activate  # Windows 11
   - source venv/bin/activate  # For Unix/Linux/Mac
   - pip install Flask Flask-RESTful

## IDE utilizado

VS Code.

## Breve descripción de los paquetes que instalamos:

Flask: El framework web que usaremos para crear nuestra pasarela API.
Flask-RESTful: Una extensión para Flask que simplifica la creación de API REST.
Creación de la puerta de enlace de API de Flask
Ahora que tenemos nuestro entorno configurado, vamos a crear una puerta de enlace de API sencilla. Crea un nuevo archivo llamado y ábrelo en tu editor de texto favorito. 
Comenzaremos importando las librerías necesarias e inicializando nuestra aplicación Flask: app.py

from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## Ejecución de la puerta de enlace de API, utilice el siguiente comando en el terminal:
  - python app.py

## Acceso a los servicios

Puede acceder a los servicios navegando y utilizando un navegador web o una herramienta de prueba de API como Postman.
  - http://127.0.0.1:5000/serviceA 
  - http://127.0.0.1:5000/serviceB 
  - http://127.0.0.1:5000/serviceC

## Implementación de funcionalidades de API Gateway
Ahora que tenemos una puerta de enlace de API básica configurada, podemos mejorar su funcionalidad. Implementemos funciones como el equilibrio de carga y la agregación de solicitudes. Para lograr el equilibrio de carga, podemos definir 
varias instancias de un servicio en nuestra puerta de enlace de API y elegir aleatoriamente una para responder a las solicitudes entrantes.

## Conclusión

Con estos conocimientos básicos, puede comenzar a crear funcionalidades más complejas en su puerta de enlace de API, como la integración con bases de datos, la implementación de mecanismos de autenticación y la adición de capacidades de monitoreo y registro. 
