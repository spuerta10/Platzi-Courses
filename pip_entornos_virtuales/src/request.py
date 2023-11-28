import requests

def making_a_request():
    API_ENDPOINT = "https://api.escuelajs.co/api/v1/categories"
    request = requests.get()
    request.status_code #estado de la peticion
    request.text #texto de la respuesta 
    categories = request.json() #jsonificar la peticion


if __name__ == "__main__":
    pass