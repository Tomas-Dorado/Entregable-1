import Ejercicio_1
import Ejercicio_2
import Ejercicio_3
# import Ejercicio_4
# import Ejercicio_5
# import Ejercicio_6
# import Ejercicio_7

# Importa los módulos de cada ejercicio

def main():
    while True:
        print("\nMenú de Ejercicios")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Ejercicio 5")
        print("6. Ejercicio 6")
        print("7. Ejercicio 7")
        print("8. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                Ejercicio_1.main()
            elif opcion == 2:
                Ejercicio_2.main()
            elif opcion == 3:
                Ejercicio_3.main()
            elif opcion == 4:
                Ejercicio_4.main()
            elif opcion == 5:
                Ejercicio_5.main()
            elif opcion == 6:
                Ejercicio_6.main()
            elif opcion == 7:
                Ejercicio_7.main()
            elif opcion == 8:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
