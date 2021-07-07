with open("input.txt","r") as f:
    ws = f.read().split()
    s = set(ws)
    dc = {i : ws.count(i) for i in s}
    for word, amount in dc.items():
        print(word,":",amount)