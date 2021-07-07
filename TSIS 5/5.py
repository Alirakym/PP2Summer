with open("input.txt","r") as f:
    lines = []
    s = f.readline()
    while s!="":
        lines.append(s)
        s = f.readline()
    print(lines)