import random

a = [random.randint(1, 100) for i in range(1, random.randint(1, 10))]

print(f"First list : {a}")
print(f"Even list : {[i for i in a if i % 2 == 0]}")
