def arreglar_texto(texto):
    '''
    Esta función recibe un texto y lo arregla para que sea más fácil de leer. 
    La receta debe tener un formato de Receta: nombre, Calorías: número. '''
    texto = texto[::-1]
    lista_de_texto = texto.replace(":", "").replace(",", "").split(" ")
    return lista_de_texto

def main():
    texto_extraido = "052 :sáirotaloc, satatap :atecéR"
    lista_de_texto = arreglar_texto(texto_extraido)
    recipe_name = lista_de_texto[1]
    calories = lista_de_texto[3]
    lectura = f"Receta: {recipe_name}\nCalorías: {calories}"

    print(lectura)

if __name__ == "__main__":
    main()