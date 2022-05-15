def read():
    number=[]
    #El modo R solo permite lectura
    with open("archivos/archivos.txt","r", encoding="utf-8") as f:
        for line in f:
            number.append(int(line))
    print(number)


def write():
    names = ["Lorena", "Diego", "Fernando", "Paola", "Karen"]
    #El modo W sobre escirbe la información
    #El modo A inclye la iunformación como adicional
    with open("archivos/names.txt", "a", encoding="utf-8") as f:
        for name in names :
            f.write(name)
            f.write("\n")
    

def run():
    print(read())
    write()

if __name__ == '__main__':
    run()