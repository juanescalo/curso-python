def squareNaturalNums(iter):
    list = []
    
    for i in range(1, iter+1):
        list.append(i**2)

    print("Lista de numeros naturales al cuadrado", list)


def run():
    x = int(input("Cuantas iteraciones deseas?: "))
    squareNaturalNums(x)


if __name__ == "__main__":
    run()