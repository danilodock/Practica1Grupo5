# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias y código
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponer el puerto donde corre Flask
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]