import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    dado = list(range(1,7)) #lista con los numeros del 1 - 6
    for _ in range(numero_de_tiros):
        tiro = random.choice(dado)
        secuencia_de_tiros.append(tiro)
    
    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = [] #resultados de las simulaciones
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros) #resultado de tirar el dado n veces
        tiros.append(secuencia_de_tiros)
    tiros_con_1 = 0
    for tiro in tiros:
        if 1 in tiro:
            tiros_con_1 += 1
    
    probabilidad_tiros_con_1 = tiros_con_1/numero_de_intentos
    print(f"Probailidad de obtener un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}")

if __name__ == "__main__":
    numero_de_tiros = 1 #cuantas veces se va a tirar el dado
    numero_de_intentos = 1000 #cuantas veces se quiere correr la simulacion
    """mientras mas veces se corre la simulacion se acerca cada vez mas a la respuesta correcta
    ley de los grandes numeros: mientras mas muestras de una poblacion mas nos acercamos a los valores reales de las probabilidades"""
    
    main(numero_de_tiros, numero_de_intentos)
    print(((1/6)*(1/6))**10)