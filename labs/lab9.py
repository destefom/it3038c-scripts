import json
import requests

r = requests.get("C:/Administrator/it3038c-scripts/labs/widgets.json")
data=r.json()

print(data['Widget'][0]['description'])