with open("input.txt","r") as f:
    a = f.read().split()
with open("input.txt","w") as f:
    f.write(str(a))