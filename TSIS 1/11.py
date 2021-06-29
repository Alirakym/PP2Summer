age = 11
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.5
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars.\n"
print(myorder.format(quantity, itemno, price))


txt = "We are the so-called \"Vikings\" from the north."
print(txt)

bxt = 'it\'s \tmy \nname i am from \\kazakhstan \n'
print(bxt)

p = "I have a {carname}, it is a {model}."
print(p.format(carname = "Ford", model = "Mustang"))