def clasificar_personajes(personajes):
    """
    Clasifica una lista de personajes en humanos y no humanos.

    Args:
        personajes (list): Lista de diccionarios con información de los personajes.
                           Cada diccionario debe tener una clave 'tipo' que indique si es 'humano' o 'no humano'.

    Returns:
        tuple: Dos listas ordenadas, la primera con personajes humanos y la segunda con personajes no humanos.
    """
    humanos = sorted([p for p in personajes if p.get('tipo') == 'humano'], key=lambda x: x.get('nombre', ''))
    no_humanos = sorted([p for p in personajes if p.get('tipo') == 'no humano'], key=lambda x: x.get('nombre', ''))
    return humanos, no_humanos


# Ejemplo de uso
def main():
    personajes = [
        {'nombre': 'Mario', 'tipo': 'humano'},
        {'nombre': 'Luigi', 'tipo': 'humano'},
        {'nombre': 'Bowser', 'tipo': 'no humano'},
        {'nombre': 'Yoshi', 'tipo': 'no humano'},
        {'nombre': 'Peach', 'tipo': 'humano'}
    ]

    humanos, no_humanos = clasificar_personajes(personajes)

    print("Humanos:")
    for humano in humanos:
        print(humano)

    print("\nNo Humanos:")
    for no_humano in no_humanos:
        print(no_humano)

if __name__ == "__main__":
    main()