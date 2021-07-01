nums = input().split()
count = 0
for i in range(len(nums)):
    j=i-count
    if nums[j] == '0':
        nums.append(nums.pop(j))
        count += 1

for i in range(len(nums)):
    print(nums[i], end=' ')