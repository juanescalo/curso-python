def run():
    x = int(input("Cuantas iteraciones deseas?: "))
    list = [i**2 for i in range(1, x+1) if i % 3 != 0]
    
    print("Lista de numeros naturales al cuadrado a excepción de los divisibles entre 3: ", list)


if __name__ == "__main__":
    run()