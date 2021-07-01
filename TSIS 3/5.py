nums = input().split()
k=int(input())
if (k < 0):
    k=abs(k)
    for i in range(k):
        nums.append(nums.pop(0))
else:
    for i in range(k):
        nums.insert(0,nums.pop())

print(*nums)


