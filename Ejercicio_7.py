def agregar_item(inventario, item):
    """
    Agrega un ítem al inventario si no está repetido.
    En caso de estar repetido, aparecera un error.
    """
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    inventario.append(item)

def main():
    inventario = []
    while True:
        item = input("Introduce un ítem para añadir al inventario (o escribe 'salir' para terminar): ")
        if item.lower() == 'salir':
            break
        try:
            agregar_item(inventario, item)
            print(f"Ítem '{item}' añadido al inventario.")
        except ValueError as e:
            print(e)
    print("Inventario final:", inventario)

if __name__ == "__main__":
    main()