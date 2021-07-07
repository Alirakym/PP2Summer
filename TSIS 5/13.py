with open("input.txt","r") as f:
    txt = f.read()
with open("output.txt","w") as f:
    f.write(txt)
    print(txt)