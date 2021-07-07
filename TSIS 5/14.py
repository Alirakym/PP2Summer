with open("input.txt","r") as f1,open("output.txt","r") as f2:
    for l1,l2 in zip(f1,f2):
        print(l1+l2)