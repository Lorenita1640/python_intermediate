#Funciones de order superior son las  funciones que reciben funciones como parametro para hacer algo con ella

#Funciones de orden superior clasicas e importantes

#Filter --> Filtra la lista

from functools import reduce


my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 !=0, my_list))
#Recibe dos parametros funcion y un iterable
print(odd)

#map --> Transformar

list_map = [1,2,3,4,5]
#double_num = [x**2 for x in list_map]
#print(double_num)
squares = list(map(lambda x: x**2, list_map))
print(squares)

#reduce
list_reduce = [2,2,2,2,2]
"""
all_multiplied = 1

for i in list_reduce :
    all_multiplied = all_multiplied*i

print(all_multiplied)
"""
all_multiplied = reduce(lambda a,b: a*b, list_reduce)
print(all_multiplied)