string = input()
print('Upper ', sum(True for letter in string if letter.isupper()))
print('Lower ', sum(True for letter in string if letter.islower()))