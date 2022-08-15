import random

def run():
    words = []
    selection = []
    print_word = []
    lifes = 20

    with open("./archivos/listado-general.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(str(line))
    
    random_word = ((random.choice(words)).strip()).lower()
    large = len(random_word)
    
    for i in range(1, large + 1):
        selection.append(random_word[(i - 1):i:1])
        print_word.append("_")

    while lifes > 0:
        print("\n")
        print(print_word)
        user_letter = str(input("Ingresa una letra: "))
        move = 0

        for letter in selection:
            if letter == user_letter:
                print_word[move] = letter
                large -= 1
            move += 1

        if large == 0:
            print("\n")
            print(print_word)
            break

        lifes -= 1
    
    if lifes == 0:
        print("Perdiste!! sólo tenías 20 vidas, la palabra era: " + random_word)
    else:
        print("Ganaste!! la palabra era: " + random_word)


if __name__ == "__main__":
    run()