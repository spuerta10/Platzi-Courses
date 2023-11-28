import requests
from lxml import html as html #archivo de texto html a archivo en el cual se puede aplicar Xpath
import os #crear una carpeta con la fecha de hoy para guardar las noticias
import datetime #traer la fecha de hoy



HOME_PAGE = 'https://www.larepublica.co/'
X_LINK = '//h2/a/@href' #link a articulos 
X_TITLE = '//h2[@data-h = "45"]/span/text()' #titulo de las noticias
X_SUMMARY = '//div[@class = "lead"]/p/text()' #resumen de la noticia
X_BODY = '//div[@class = "html-content"]/p/text()' #parrafos de la noticia


def get_article(link, today): #acceder a los links para obtener la noticia
    try:
        response = requests.get(link) #varibale que contiene la respuesta a la peticion
        if response.status_code == 200: #si el servidor me contesta que todo bien 
           html_article = response.content.decode('utf-8')
           Xpath = html.fromstring(html_article) #transforma el doc html a doc especial en el cual puedo usar Xpath
           try: #traer titulo, resumen y cuerpo
                title = Xpath.xpath(X_TITLE)[0] #traigo el primer elemento el cual tiene estar en el indice 0
                title = title.replace('\"','') #eliminar posibles comillas del titulo
                summary = Xpath.xpath(X_SUMMARY)[0]
                body = Xpath.xpath(X_BODY)
           except IndexError: #si no puedo extraer titulo, resumen o cuerpo dar error
                return
            
           with open(f'{today}/{title}.txt','w',encoding='utf-8') as f: #buscar la carpeta con la fecha creada y dentro de la carpeta guardar la noticia
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for paragraph in body: #el cuerpo es una lista de parrafos, escribir cada parrafo que hay en el cuerpo de la noticia
                    f.write(paragraph)
                    f.write('\n')
        else: #si el servidor me tira algun error
            raise ValueError(f'Error: {response.status_code}') #decir que el servidor reporto un error en la respuesta a la peticion
    except ValueError as err:
        print(err)


def get_links(): #funcion para extraer los links de las noticias
    try:
        response = requests.get(HOME_PAGE) #varibale que contiene la respuesta a la peticion
        if response.status_code == 200: #si el servidor me contesta que todo bien 
            html_doc = response.content.decode('utf-8')
            Xpath = html.fromstring(html_doc) #transforma el doc html a doc especial en el cual puedo usar Xpath
            links = Xpath.xpath(X_LINK) #links a las demas noticias
            #print(links)

            today = datetime.date.today().strftime('%d-%m-%Y') #traer la fecha de hoy en el formato dia, mes, año
            if not os.path.isdir(today): #si no existe una carpeta con la fecha de hoy, crearla
                os.mkdir(today)
            
            for l in links: #entrar en cada link y extraer la noticia y guardarla con la fecha
                get_article(l, today)

        else: #si el servidor me tira algun error
            raise ValueError(f'Error: {response.status_code}') #decir que el servidor reporto un error en la respuesta a la peticion
    except ValueError as err:
        print(err)

def run():
    get_links()


if __name__ == '__main__':
    run()



