def run():

    """
    square=[]
   
    for i in range (101):
        if i%3 == 0 :
            print("Pase por aquí con ->",i)
        else :
            square.append(i*i)
    
    print(square)
    """

    # squares = [i**2 for i in range (1,101) if i % 3 != 0] 

    #Reto
    
    reto = [i for i in range (1,10000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(reto)


if __name__ == '__main__':
    run()