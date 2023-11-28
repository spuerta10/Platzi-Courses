'''Scraper de precio historico de dolar vs peso colombiano en junio del año 2008'''

import matplotlib.pyplot as plt
import requests
from lxml import html as html
import numpy as np
import matplotlib.pyplot as plt


PAGE = 'https://www.dolar-colombia.com/mes/2008-06'
DATES = '//table[@class = "table-highlighted"]//a/text()'
PRICES = '//td[@class = "text-nowrap text-right"]/text()'


def arr_float(arr):
    f_arr = arr.astype(np.float)
    return f_arr


def remove_char(arr): #funcion para remover de una lista un caracter en especifico
    for x in range(0, len(arr)):
        arr[x] = arr[x][0:7].replace('$ ','').replace(',','.')
    return arr

def dolar_prices():
    try:
        response = requests.get(PAGE) #respuesta del servidor
        if response.status_code == 200: #si la respuesta del servidor es Ok(200)
            doc = response.content.decode('utf-8')
            x_doc = html.fromstring(doc)
            dates = x_doc.xpath(DATES)
            s_prices = x_doc.xpath(PRICES) #string de cambio dolar a cop
            prices = remove_char(s_prices)
            plots(prices, dates)

        else: #si el servidor no me da OK(200)
            raise ValueError(f'Error: {response.status_code}')#mostrar el error que me da el servidor 
    except ValueError as err:
        print(err)

def plots(price, date):
    plt.plot(date, price, color = 'orange')
    plt.xlabel('fecha')
    plt.ylabel('valor')
    plt.title('junio vs valor dolar(cop) 2008')
    plt.show()

def run():
    dolar_prices()

if __name__ == '__main__':
    run()
