# fastAPI usa uvicorn, uvicorn lanza y mantine en linea el servicio construido en fastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 


'''
Para ejecutar es necesario el siguiente comando
uvicorn nombre_archivo:nombre_aplicacion --reload
'''


app = FastAPI()


@app.get('/categories', response_class=HTMLResponse) #responder template HTML
def get_categories():
    API_ENDPOINT = ""