def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"Firstname": "Juan", "Lastname": "Escandón"}

    super_list = [
        {"Firstname": "Juan", "Lastname": "Escandón"},
        {"Firstname": "Camilo", "Lastname": "López"},
        {"Firstname": "Ricardo", "Lastname": "Calixto"},
        {"Firstname": "María", "Lastname": "Acosta"},
        {"Firstname": "Nelsy", "Lastname": "Hernández"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "float_nums": [1.1, 4.5, 6.4]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in range (len(super_list)):
        for key, value in super_list[i].items():
            print(key, "-", value)


if __name__ == "__main__":
    run()