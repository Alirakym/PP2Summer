with open("input.txt","r") as f:
    text = "".join([f.readline() for i in range(int(input()))])
print(text)