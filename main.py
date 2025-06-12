from flask import Flask, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


url_pura = "http://api.weatherapi.com/v1/current.json"
chave_api = os.getenv("key")

url = f"{url_pura}?key={chave_api}&q=guarulhos"
request = requests.get(url)
clima_geral = request.json()
clima_city = clima_geral['current']['temp_c']

if __name__ == '__main__':
    app.run(debug=True)