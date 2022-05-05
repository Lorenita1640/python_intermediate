import math


def run():
    """
    reto1 = {}

    for key in range(1,101):
        if key % 3 != 0:
            reto1[key] = key**3

    print(reto1)
    

    my_dictionary = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dictionary)
    """

    reto2 = {i: round(math.sqrt(i),2) for i in range(1,1000)}
    print(reto2)

if __name__ == '__main__':
    run()