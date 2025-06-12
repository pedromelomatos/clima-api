import requests
from dotenv import load_dotenv
import os

load_dotenv()

url_pura = "http://api.weatherapi.com/v1/current.json"
chave_api = os.getenv("key")

url = f"{url_pura}?key={chave_api}&q=London"
request = requests.get(url)
clima = request.json()
print(clima)

