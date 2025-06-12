from flask import Blueprint, render_template, request, redirect, url_for
import requests
from dotenv import load_dotenv
import os

load_dotenv()

cidade_escolhida = Blueprint('cidade_escolhida_bp', __name__, template_folder='templates')

@cidade_escolhida.route("/clima/<cidade>", methods=['GET', 'POST'])
def clima(cidade):
    if request.method == 'GET':    
        url_pura = "http://api.weatherapi.com/v1/current.json"
        chave_api = os.getenv("key")

        url = f"{url_pura}?key={chave_api}&q={cidade}"
        request_api = requests.get(url)
        clima_geral = request_api.json()
        clima_city = clima_geral['current']['temp_c']
        
        return render_template("clima.html", clima_city=clima_city)
    elif request.method == 'POST':
        cidade = request.form['cidadeinput'].lower()
        return redirect(url_for('cidade_escolhida_bp.clima', cidade=cidade))