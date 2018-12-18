import random

list_a = [random.randint(0, 5) for i in range(random.randint(0, 20))]
print(f"Generated list: {list_a}")

# TODO: Time these to see which is faster as the list grows
def unique_by_iter(a):
    unique = []
    for i in a:
        if i not in unique:
            unique.append(i)
    return unique


def unique_by_set(a):
    return list(set(a))


print(f"Unique by iteration: {unique_by_iter(list_a)}")
print(f"Unique by set: {unique_by_set(list_a)}")
