nums = []
count = 0
n = int(input())

for i in range(0,n): 
    elem = int(input()) 
    nums.append(elem)

print(nums)
for i in range(0,n):
    for j in range(0,n):
        if i<j and nums[i]==nums[j]:
            count+=1

print(count)