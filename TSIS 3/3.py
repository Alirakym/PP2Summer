nums = list(map(int,input().split()))

for i in range(0, len(nums)):
    print(nums[len(nums)-i-1],end=" ")
