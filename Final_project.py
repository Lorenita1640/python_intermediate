from hashlib import new
import random
import os
import numpy as np
import turtle as tl
import sys

def run():
    word = data()
    init(word)

def data():

    words=[]

    with open("archivos/data.txt","r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
    
    max = len(words)
    rand = random.randint(0,max)
    word = words[rand]
    print("aqui 0-->", word)
    return word

def init(word):
    word = [i for i in word if i != "\n"]
    new_word = ["-" for i in  word if i != "\n"]

    draw(word, new_word, 0,0)


def fill_in(word,new_word,count):

    letter = input("Por favor ingrese una letra: ")

    check = check_word(letter, word,new_word,count)
    print("Aqui en fill: ", check)
    
    new_word = check[0]
    count = check[1]
    flag = check[2]

    if new_word == word:
        tl.bye()
        sys.exit("GANASTE")  
    else :
        draw(word,new_word,count,flag)

def draw(word,new_word,count,flag):
    os.system("clear")

    if count == 1 and flag == 1 :
        tl.setup(400, 450, 1200,50)
        tl.bgcolor("black")
        tl.color("White")
        tl.speed(3)
        tl.width(2)
        tl.penup()
        tl.goto(150,-150)
        tl.pendown()
        tl.left(180)
        tl.fd(70)
        tl.lt(180)
        tl.fd(35)
        tl.lt(90)
    elif count == 2 and flag == 1:
        tl.fd(300)
        tl.lt(90)
    elif count == 3 and flag == 1:
        tl.fd(150)
        tl.lt(90)
    elif count == 4 and flag == 1:
        tl.fd(70)
        tl.lt(90)
    elif count == 5 and flag == 1:
        tl.bgcolor("orange")
        tl.dot(35)
    elif count == 6 and flag == 1:
        tl.lt(270)
        tl.fd(120)
    elif count == 7 and flag == 1:
        tl.lt(45)
        tl.fd(30)
        tl.lt(180)
        tl.fd(30)
    elif count == 8 and flag == 1:
        tl.bgcolor("red")
        tl.lt(90)
        tl.fd(30)
        tl.lt(180)
        tl.fd(30)
        tl.lt(45)
    elif count == 9 and flag == 1:
        tl.fd(60)
        tl.lt(90)
    elif count == 10 and flag == 1:
        tl.fd(35)
        tl.lt(180)
        tl.fd(70)
        tl.bye()
        sys.exit("PERDISTE")       
                  
    
    print(new_word)

    fill_in(word,new_word,count)


def check_word(letter, word,new_word,count):

    word = np.array(word)
    indexs = np.where(word == letter)
    indexs = indexs[0]
    flag = 0
    if count == "-" :
        count = count

    if indexs.size == 0:
        count = count+1
        flag = 1
        print("Aqui contador : ", count)
        return new_word, count, flag
        
    else:
        for indx in indexs:
            new_word[indx] = letter
        return new_word, count, flag

    

if __name__ == '__main__':
    run()