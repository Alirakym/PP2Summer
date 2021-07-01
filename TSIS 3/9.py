N, M = input().split()
N = int(N)
M = int(M)
Anya=set()
Borya=set()
for i in range(N):
    Anya.add(int(input()))

for i in range(M):
    Borya.add(int(input()))
print('\n')
print(len(Anya & Borya))
print(*[str(item) for item in sorted(Anya & Borya)])

print(len(Anya - Borya))
print(*[str(item) for item in sorted(Anya - Borya)])

print(len(Borya - Anya))
print(*[str(item) for item in sorted(Borya - Anya)])