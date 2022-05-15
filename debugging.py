def divisors(num):

    """
    
    #Original

    divisor = [ i for i in range(1, num + 1) if num % i == 0]
    return divisor
    """

    """
    Clase de manejo Try, except, raise y Finally
    try:
        if num <= 0 :
            raise ValueError("Por favor ingrese un numero positivo")

        divisor = [ i for i in range(1, num + 1) if num % i == 0]
        return divisor

    except ValueError as ve:
            print(ve)
    """

    #Clase Assert statements
    assert num>=0, "Debes ingresar un número positivo"
    divisor = [ i for i in range(1, num + 1) if num % i == 0]
    return divisor

def run():

    """
    #Original
    print(divisors(num = int(input("Ingresa un numero:"))))
    print("termino mi programa")
    """

    """
    Clase de manejo Try, except, raise y Finally

    try:
        print(divisors(num = int(input("Ingresa un numero:"))))
        print("termino mi programa")

    except ValueError:
            print("Debes ingresar un valor numerico")
    """

    #Clase Assert statements

    num = input("Ingresa un numero:")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("termino mi programa")


if __name__ == '__main__':
    run()



