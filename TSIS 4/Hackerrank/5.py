import re
s, k = map(lambda x:x,[input() for i in range(2)])
for i in re.finditer("(?<="+k+")",s):
    print((i.start()-len(k),i.end()-1))
if not re.search(k,s):
    print((-1,-1))