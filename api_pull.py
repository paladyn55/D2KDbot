import requests
import json
response_API = requests.get('https://destinytracker.com/')
data = response_API.text
json.loads(data)