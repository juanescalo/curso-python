def squareNaturalNums(iter):
    list = []
    
    for i in range(iter):
        list.append((i+1)**2)

    print("Lista de numeros naturales al cuadrado", list)


def run():
    x = int(input("Cuantas iteraciones deseas?: "))
    squareNaturalNums(x)


if __name__ == "__main__":
    run()