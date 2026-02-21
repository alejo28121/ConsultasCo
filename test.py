import requests

url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"

params = {
    "$limit": 1,
    "$where": "departamento_nom='RISARALDA'"
}

r = requests.get(url, params=params, timeout=30)

print("Status:", r.status_code)
print("Data:", r.json())
