# -*- coding: utf-8 -*-

# Importamos librerias necesarias
import requests
import re
from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)


@app.errorhandler(405)
def page_not_found(e):
    '''
    Function: page_not_found
    Summary: En caso de usar un método diferente al GET, mostramos error
    Attributes:
        @param (e):exceptions
    Returns: json response
    '''
    response = jsonify({'error': 'Metodo HTTP no permitido'})
    response.status_code = 405
    return response


@app.route('/commit', methods=['POST'])
def git_commit():
    '''
    Function: git commit
    Summary: Se recibe el JSON de GitHub cuando se hace commit
    Examples: POST HTTP/1.1 { "json":"json"}
    Attributes:
    Returns: 
    '''
    # Obtenemos respuesta del commit dde GIT
    git_json = json.loads(request.data)
    # Obtenemos Repositorio
    repo = git_json['repository']['full_name']
    # Obtenemos Branch ("ref":"refs/heads/devel")
    branch = git_json['ref'].split('/')[2]
    # Obtenemos version del Docker si no se envia, se asume version en deploy
    docker = git_json['head_commit']['message'].split('->')[1]
    return "True" 

# Inicializamos un servidor web en el puerto 80 (puerto por defecto 5000)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
