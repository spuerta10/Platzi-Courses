#dockerfile para un Script


#desde que version de python quiero correr el contenedor
FROM python:3.8 
#crear mi entorno de trabajo con la carpeta app
WORKDIR /app 
#copio el archivo requeriments de mi local y lo paso al contenedor
COPY requirements.txt /app/requirements.txt
#instalo las dependencias especificadas en el archivo
RUN pip install --upgrade -r /app/requeriments.txt
#copiar todo lo que hay en el directorio donde estoy parado y llevarlo a la carpeta app
COPY . /app
#lanzar el servidor de uvicorn
CMD  {"uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"}