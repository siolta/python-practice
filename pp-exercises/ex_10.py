import random

a = [random.randint(0, 50) for i in range(random.randint(0, 20))]
b = [random.randint(0, 50) for i in range(random.randint(0, 20))]


def commons(a, b):
    a_I = 0
    b_I = 0
    c = []
    which_min = a if len(a) < len(b) else b

    for i in range(len(which_min)):
        if a[a_I] > b[b_I]:
            c.append(a[a_I])
            a_I += 1
        elif b[b_I] > a[a_I]:
            c.append(b[b_I])
            b_I += 1
        elif a[a_I] == b[b_I]:
            if a[a_I] not in c:
                c.append(a[a_I])
            if len(a) < len(b):
                a_I += 1
            else:
                b_I += 1

    return c


print(commons(a, b))
