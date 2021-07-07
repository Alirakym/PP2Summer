import re
n = int(input())
for i in range(n):
    a = input()
    print(bool(re.search('[0-9]*\.[0-9]+|[\+\-][0-9]*\.[0-9]+',a)) and not bool(re.search('[^0-9\.\+\-]',a)) and 
    not bool(re.search('[0-9]+[\+\-]',a)) and len(re.findall('[\+\-]',a))<2 and len(re.findall('[\.]',a))==1)