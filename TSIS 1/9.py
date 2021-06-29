a = "Hello, World!"
print(a[1])
print(len(a))
for a in "Hello, World!":
  print(a)
print(len(a))

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" in txt:
  print("Yes, 'expensive' is present.")
elif "expensive" not in txt:
    print("'expensive' is NOT present.")


    b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-13:-2])


c = "         Hello, World! "
print(c.strip())


d = "Hello, World!"
print(d.replace("o", "x"))


e = "Hello World!"
print(e.split("W"))