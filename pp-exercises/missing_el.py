import random

ordrd_lst = [i for i in range(1, 100)]
ordrd_lst.pop(random.choice(ordrd_lst))

el_index = 0

for el in ordrd_lst:
    if el_index == el - 1:
        el_index += 1
    else:
        print(f"Missing element is: {el - 1}")
        el_index = 0
        break
