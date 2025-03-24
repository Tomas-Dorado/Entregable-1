def descomponer_ip(direccion_ip):
    '''Agarra la dirección IP y la descompone en octetos, comprobando que sea válida'''
    try:
        octetos = direccion_ip.split('.')
        print(octetos)
        if len(octetos) != 4 or not all(0 <= int(octeto) <= 255 for octeto in octetos):
            raise ValueError("Dirección IP inválida")
        for i, octeto in enumerate(octetos, start=1):
            print(f"Octeto {i}: {octeto}")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    direccion_ip = input("Introduce una dirección IP (xxx.xxx.xxx.xxx): ")
    descomponer_ip(direccion_ip)

if __name__ == "__main__":
    main()

