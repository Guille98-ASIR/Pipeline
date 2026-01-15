# 1. Imagen base ligera de Python
FROM python:3.11-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar todos los archivos de tu repositorio al contenedor
COPY . .

# 4. Comando para ejecutar tu agenda
# -u asegura que los mensajes de Python se vean en tiempo real en Jenkins
CMD ["python", "-u", "ej1.py"]
