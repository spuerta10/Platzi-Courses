#convertir de peso colombiano a dolar
def divisa(cop):
    dolar = cop/3595.42
    return dolar

if __name__ == '__main__':
    cop = float(input("Digite los pesos colombianos."))
    dolar = divisa(cop)
    print(f"El equivalente de {cop} pesos es de {round(dolar,2)} dolares.")

