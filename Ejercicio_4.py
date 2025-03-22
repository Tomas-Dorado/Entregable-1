def main():
    misiones = [
        (1, "Misión: Tutorial"),
        (3, "Misión: Rescatar al aldeano"),
        (2, "Misión: Explorar la cueva"),
        (5, "Misión: Derrotar al dragón"),
        (4, "Misión: Defender el castillo")
    ]

    # Ordenar las misiones por el nivel de dificultad
    misiones.sort(key=lambda x: x[0])

    print("Misiones ordenadas por dificultad:")
    for _, mision in misiones:
        print(mision)

if __name__ == "__main__":
    main()
