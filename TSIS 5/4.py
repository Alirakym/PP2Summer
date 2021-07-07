n = int(input())
with open("input.txt","r") as f:
    lines = f.readlines()
print(''.join(lines[-n:]))