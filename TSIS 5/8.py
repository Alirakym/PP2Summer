with open("input.txt","r") as f:
    w = f.read().split()
    mx = len(max(w,key=len))
    print([i for i in w if len(i) == mx])