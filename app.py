from flask import Flask, jsonify, request   
import random

app = Flask(__name__)

@app.route('/')
def home(): #Ruta principal
    return jsonify({'message': 'Api Grupo5'}) #Retorna un mensaje en formato JSON

@app.route('/api/USDtoEUR', methods=['POST']) 
def convertirUSD(): 
    data = request.get_json() #Obtener los datos enviados en formato JSON
    # Validar que venga el campo 'usd'
    usd = data.get('usd')
    if usd is None:
        return jsonify({"error": "Se requiere un valor 'usd'"}), 400

    # Validar que sea numérico (int o float)
    try:
        usd = float(usd)
    except (ValueError, TypeError):
        return jsonify({"error": "El valor debe ser numérico"}), 400

    # Validar que sea positivo
    if usd <= 0:
        return jsonify({"error": "El valor debe ser un número positivo"}), 400

    # Si pasa todas las validaciones, hacer la conversión
    resultado = usd * 0.85
    return jsonify({"resultado": resultado}), 200



frases = [
    "Pensamiento de Danilo: Nunca pares de aprender 📚",
    "Pensamiento de Paul: El código es poesía 💻",
    "Pensamiento de Danny: Cada error es una oportunidad 🔧",
    "Pensamiento gerenal: La creatividad es tu mejor herramienta 🎨"
]

@app.route('/api/frase', methods=['GET'])
def frase():
    return jsonify({"frase": random.choice(frases)})

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=8080)
