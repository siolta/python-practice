import time

name = input("What's your name? ")
age = input("What's your age? ")

_year = time.localtime()[0]
diff = 100 - int(age)

print(f"Congrats {name}, you will turn 100 in year {_year + diff}")
