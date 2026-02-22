import requests

def request_convertirUSD(usd):
    url = 'http://localhost:8080/api/USDtoEUR'
    data = {"usd": usd}
    response = requests.post(url, json=data)
    return response.json()

respuesta = request_convertirUSD("th")
print("Resultado de convertir USD a Euro es:", respuesta)


def request_frase():
    url = 'http://localhost:8080/api/frase'
    response = requests.get(url)
    return response.json()

frase = request_frase()
print("La frase del dia es:", frase)