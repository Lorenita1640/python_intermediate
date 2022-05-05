def run():

    #Clase diccionarios y listas anidadas
    my_list = [ 1 , "Hello" , True , 4.5 ]
    my_dicc = {"Firstname":"Lorena", "LastName":"Escobar"}

    super_list = [
        {"Firstname":"Lorena", "LastName":"Escobar"},
        {"Firstname":"Lorena2", "LastName":"Escobar2"},
        {"Firstname":"Lorena3", "LastName":"Escobar3"},
        {"Firstname":"Lorena4", "LastName":"Escobar4"},
        {"Firstname":"Lorena5", "LastName":"Escobar5"}
    ]

    super_dict = {
        "natural_nums": [1 , 2, 3, 4, 5],
        "int_nums": [-1 , -2, 0, 1, 2],
        "float_nums": [1.1 , 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

    for item in super_list:
        print(item["Firstname"], "-", item["LastName"])
    


if __name__ == '__main__':
    run()