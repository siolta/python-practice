import random

a = [random.randint(0, 50) for i in range(random.randint(0,20))]
b = [random.randint(0, 50) for i in range(random.randint(0,20))]

new_list = []

print(f"List a: {a}")
print(f"List b: {b}")

for i in a:
    if i not in new_list:
        new_list.append(i)

for i in b:
    if i not in new_list:
        new_list.append(i)

print(sorted(new_list))
