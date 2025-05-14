# Creación de un modelo estimador de Trading con Flask, Pandas y SQLite3

* Autor: Neobytes84
* Project_URL: https://github.com/neobytes84/estimator_trading_flask

Flask es un framework web de Python ligero y flexible. 
Predecir los precios de las acciones siempre ha sido uno de los desafíos más emocionantes para los científicos de datos y los analistas financieros. Flask es un framework web de Python ligero y flexible, el cual permite crear aplicaciones web simples rápidamente 
y lo hace ideal para crear una API de predicción de acciones, estimaciones de costos, generar historial de transacciones para estudiar patrones o eventos que nos permitan tomar decicisiones frente a una oportunidad de inversiones financieras.

## Objetivos

  - Configuración un entorno de Flask
  - Implementación de rutas y funcionalidades en Flask que actúen como puerta de enlace de API.
  - Manejar solicitudes y respuestas hacia y desde varios servicios.
  - Implementación la puerta de enlace de API y pruebe su funcionalidad.

## Configuración del entorno

 Asegúrese de tener Python 3.13.0 instalado en su sistema. Una vez instalado puede crear un entorno virtual e instalar Flask.
 
## Creación de carpeta, entorno virtual e instalación de Flask 
   - mkdir trading-flask
   - cd trading-flask
   - python -m venv ven
   - .\ven\Scripts\activate  # Windows 11
   - source venv/bin/activate  # For Unix/Linux/Mac
   - pip install Flask
   - pip install Pandas

## IDE utilizado

VS Code.

## Breve descripción de los paquetes que instalamos:

Flask: El framework web que usaremos para crear nuestra pasarela API.
Pandas: librería de Python, especializada en la manipulación, operaciones y estructura de datos fundamentales para desarrollar e implementar el análisis de datos.
SQLIte3: sistema de gestión de base de datos

from flask import Flask, jsonify
import pandas as pd
import sqlite3

app = Flask(__name__)
api = Api(app)

## Ejecución de la puerta de enlace de API, utilice el siguiente comando en el terminal:
  - python estimator_trading.py

## Acceso a los servicios

Puede acceder a los servicios navegando y utilizando un navegador web
  - http://127.0.0.1:5000/api/trading
  - http://127.0.0.1:5000/api/trading/<id_stock>
  - http://127.0.0.1:5000/api/trading/broker/<id_broker>
  - http://127.0.0.1:5000/api/trading/strategy/<id_strategy>
  - http://127.0.0.1:5000/api/trading/account/<id_account>
  - http://127.0.0.1:5000/api/trading/asset/<asset>

## Implementación de funcionalidades de API REST
El primer paso para crear la aplicación es importar Flask e inicializar la aplicación como se indicó anteriormente. Flask se encargará de las solicitudes entrantes, y devolverá los calculos financieros basados en el DataFrame que se ha creado con Pandas.
## Conclusión

Una vez ejecutada la aplicación en el servidor, se genera autoámticamente la base de datos con SQLite3 y a la par, genera archivos .csv. Este tipo de sistema nos permite implementarlo hacia una un proyecto más escalable, como por ejemplo: implementar un monitoring and logging en tiempo real, predicciones trading en tiempo real, incluso automatizar job stores y task scheduler a través de ETL(pipelines).
