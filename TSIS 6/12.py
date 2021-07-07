def palindrom(l):
    if l==l[::-1]:
        return True
    elif l!=l[::-1]:
        return False
    
print(palindrom(input()))