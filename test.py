import requests

def request_convertirUSD(usd):
    url = 'http://localhost:8080/api/USDtoEUR'
    data = {"usd": usd}
    response = requests.post(url, json=data)
    return response.json()

respuesta = request_convertirUSD(586)
print("Resultado de convertir USD a Euro es:", respuesta)

# ## Para probar con el servicio puesto en nube
# def request_convertirUSD(usd):
#     url = 'https://gagrupo5-242065751485.us-central1.run.app/api/USDtoEUR'
#     data = {"usd": usd}
#     response = requests.post(url, json=data)
#     return response.json()

# respuesta = request_convertirUSD(586)
# print("Resultado de convertir USD a Euro es:", respuesta)


def request_frase():
    url = 'http://localhost:8080/api/frase'
    response = requests.get(url)
    return response.json()

frase = request_frase()
print("La frase del dia es:", frase)


## USO DE UNA API EXTERNA PARA CONVERSION DE MONEDAS
import requests

# Definimos los parámetros de la conversión
cantidad = 100
moneda_origen = "USD"
moneda_destino = "EUR"

# Construimos la URL con los parámetros correctos
url1 = f"https://api.frankfurter.dev/v1/latest?amount={cantidad}&from={moneda_origen}&to={moneda_destino}"

# Realizamos la petición
response = requests.get(url1)

if response.status_code == 200:
    data = response.json()
    resultado = data['rates'][moneda_destino]
    print(f"{cantidad} {moneda_origen} equivalen a {resultado} {moneda_destino}")
else:
    print("Error al conectar con la API")

##NUEVO GET PARA MODIFICAR REPOSITORIO MATRIZ
def test_weather():
    # Definir latitud y longitud (ejemplo: Tokio)
    lat = 35.0
    lon = 139.0
    # Construir la URL de la API
    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
    # Hacer la petición GET
    response = requests.get(url2)
    # Convertir la respuesta a JSON
    data = response.json()
    # Mostrar parte de la respuesta
    print("Temperaturas por hora en Tokio:")
    print(data["hourly"]["temperature_2m"][:10])  # primeras 10 horas

# Ejecutar la función de prueba
if __name__ == "__main__":
    test_weather()



# #Uso de API externa con argumentos de línea de comando
# import argparse, requests

# # Definir argumentos de línea de comando
# parser = argparse.ArgumentParser(description="Conversión de monedas usando la API Frankfurter")
# parser.add_argument("--cantidad", type=float, required=True, help="Cantidad a convertir")
# parser.add_argument("--origen", type=str, required=True, help="Moneda origen (ej: USD)")
# parser.add_argument("--destino", type=str, required=True, help="Moneda destino (ej: EUR)")
# args = parser.parse_args()

# # Construir la URL con los parámetros
# url1 = f"https://api.frankfurter.dev/v1/latest?amount={args.cantidad}&from={args.origen}&to={args.destino}"

# # Realizar la petición
# response = requests.get(url1)

# if response.status_code == 200:
#     data = response.json()
#     resultado = data['rates'][args.destino]
#     print(f"{args.cantidad} {args.origen} equivalen a {resultado} {args.destino}")
# else:
#     print("Error al conectar con la API")

## Para usar el api externa por linea de comando se debe ejecutar el script de la siguiente manera:
# python test.py --cantidad 100 --origen USD --destino EUR