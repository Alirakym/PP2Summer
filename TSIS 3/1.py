nums = []
n = int(input())

for i in range(0,n): 
    elem = int(input()) 
    nums.append(elem)

for i in range(0,n+1):
    if i%2==0:
        print(nums[i],end=" ")