def main():
    lista1 = ["manzana", "pera", "uva", "naranja", "manzana"]
    lista2 = ["pera", "kiwi", "naranja", "uva", "kiwi"]

    palabras_comunes = list(set(lista1) & set(lista2))
    print("La nueva lista es: "palabras_comunes)

if __name__ == "__main__":
    main()