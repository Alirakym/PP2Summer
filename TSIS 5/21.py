abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
with open("output.txt","w") as f:
    l = len(abc)//n
    for i in range(n):
        f.write(abc[i*l:(i+1)*l]+"\n")