# Para las aplicaciones web creadas con Flask, debemos importar siempre el modulo flask
# la clase request permite acceso a la información de la petición HTTP

from flask import Flask, request, jsonify , url_for

# para poder servir plantillas HTML desde archivos, es necesario importar el modulo render_template

from flask import render_template

import sys
sys.path.append('src')

from view_web import view_web

# Flask constructor: Crea una variable que nos servirá para comunicarle a Flask la configuración que queremos para nuestra app

app = Flask(__name__)

app.register_blueprint(view_web.blueprint)

if __name__ == '__main__':
    app.run(debug=True)