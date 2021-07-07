import re
s = ''
t = 1
with open("input.txt",encoding = "utf8") as f:
    for i in f.readlines():
        s+=i
name = re.findall("ДУБЛИКАТ\n(.*)",s)[0]
BIN = re.findall("БИН(\s[0-9]*)",s)[0]
data_for_each = re.findall("\.\n(.*)\n([0-9]),.*x\s(.*)\n(.*)\nСтоимость\n(.*)",s)
title = [data_for_each[i][0] for i in range(len(data_for_each))]
coat = [data_for_each[i][1] for i in range(len(data_for_each))]
total_price = [data_for_each[i][2] for i in range(len(data_for_each))]
unit_price = [data_for_each[i][3] for i in range(len(data_for_each))]
address = re.findall("г\..*",s)[0]
time = re.findall("Время: (.*)",s)[0]
print("Название компаний: " + name)
print(" БИН: " + BIN)
print(len(BIN),len(title))
for i in range(len(title)):
    print(" Название товара: " + title[i])
    print("  Цена: " + unit_price[i])
    print("  Количество: " + coat[i] + " тыс.")
    print("  Общая цена: " + total_price[0])
print("Время: " + time)
print("Местонахождение: " + address)
f.close()