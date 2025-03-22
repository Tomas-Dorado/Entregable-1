def obtener_datos():
    '''la función pide los datos para el calculo del interés compuesto'''
    while True:
        try:
            tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))
            if 1 <= tasa_interes <= 10:
                break
            else:
                print("Por favor, introduce un valor entre 1 y 10.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    while True:
        try:
            anios = int(input("Introduce el número de años: "))
            if anios > 0:
                break
            else:
                print("Por favor, introduce un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")
    
    return tasa_interes, anios

def calcular_interes_compuesto(capital_inicial, tasa_interes, anios):
    '''Calcula el interés compuesto, pide la tasa de interés y el número de años'''
    # Calcular el interés compuesto
    tasa_interes_decimal = tasa_interes / 100
    capital_final = capital_inicial * ((1 + tasa_interes_decimal) ** anios)
    return capital_final

def main():
    capital_inicial = 1000
    tasa_interes, anios = obtener_datos()
    capital_final = calcular_interes_compuesto(capital_inicial, tasa_interes, anios)
    print(f"El capital final después de {anios} años es: {capital_final:.2f}")

if __name__ == "__main__":
    main()