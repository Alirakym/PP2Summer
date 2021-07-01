nums = list(map(int,input().split()))
minimum=nums[0]
for i in range(0, len(nums)):
    if minimum<nums[i] and nums[i]>0:
        minimum = nums[i]

for i in range(0, len(nums)):
    if minimum>nums[i] and nums[i]>0:
        minimum = nums[i]
        
print(minimum)