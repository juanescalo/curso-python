def squareNaturalNums(iter):
    list = []
    Divisive = []
    
    for i in range(1, iter+1):
        mod = i % 3
        if mod == 0:
            Divisive.append(i)
        else:
            list.append(i**2)

    print("Lista de numeros naturales al cuadrado", list)
    print("Los cuadrados excluidos fueron: ", Divisive)


def run():
    x = int(input("Cuantas iteraciones deseas?: "))
    squareNaturalNums(x)


if __name__ == "__main__":
    run()