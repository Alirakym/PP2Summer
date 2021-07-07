import glob
s = glob.glob("*.txt")
c = []
for i in s:
    with open(i,"r") as f:
        c.append(f.read())
print(c)