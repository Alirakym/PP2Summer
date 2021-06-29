nums = []
highest = 0
altitudes = []
altitudes.append(highest)
n = int(input())

for i in range(0,n): 
    elem = int(input()) 
    nums.append(elem)

for i in range(0,n):

    altitudes.append(nums[i])
    altitudes[i+1]=altitudes[i]+altitudes[i+1]
    
highest = altitudes[0]
for i in range(0,n):
    if highest<altitudes[i]:
        highest = altitudes[i]

print(nums)
print(altitudes)
print(highest)