cars = ["Ford", "Volvo", "BMW"]
x = cars[2]
print(x)
cars[0] = "Toyota"
print(cars[0],cars[1])
y = len(cars)
print(y)
for i in cars:
    print(i)
print("\n")

cars.append("Honda")
print(cars)