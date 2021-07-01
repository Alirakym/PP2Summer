N = int(input())
D = {}
for i in range(N):
    word1, word2 = input().split()
    D[word1] = word2
    D[word2] = word1
print("\n")
print(D[input()])