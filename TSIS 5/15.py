from random import randint
with open("input.txt","r") as f:
    ls = f.readlines()
    rnd = randint(0,len(ls)-1)
    print(ls[rnd])