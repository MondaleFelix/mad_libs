import json 
import requests

api_url = "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25"

r = requests.get(api_url)

data = r.json

print(data)
