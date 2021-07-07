text = input()
with open("input.txt", "a") as f:
    f.write('\n'+text)
with open("input.txt", "r") as f:
    print(f.read())