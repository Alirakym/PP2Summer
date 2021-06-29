print(1 > 9)
print(9 == 9)
print(2 < 3)

a = 33
b = 33

if b > a:
  print("b is greater than a")
  
elif b == a:
  print("b and a are equal")
  
else:
    print("b is not greater than a")

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


x = 33
print(isinstance(x, int))