import numpy as np
import random
import matplotlib.pyplot as plt


def show_function(x,y,function):
    plt.plot(x,function, color = "red")
    plt.scatter(x,y, color = "red")
    plt.show()
    print(x,y)
    
    
if __name__ == "__main__":
    x = np.array([i for i in range (0,9)]) #variable independiente
        #y = np.array([i for i in range (1,10)])
    y = np.array([random.randint(1,3) for i in range (0,9)]) #variable dependiente (resultados)
    coeffs = np.polyfit(x,y,1) #coeficientes lineales para generar funcion
    print(f"Coeficientes: {coeffs}")
    #funcion de la forma mx + b
    m = coeffs[0] #pendiente
    b = coeffs[1]
    function = (m * x) + b #linea que mejor se acomoda a los datos
    print(f"Funcion: {function}")
    show_function(x,y,function)