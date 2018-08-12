a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def commons(a, b):
    a_I = 0
    b_I = 0
    c = []
    which_min = a if len(a) < len(b) else b

    for i in range(which_min):
        if a[a_I] > b[b_I]:
            c.append(a[a_I])
            a_I += 1
        elif b[b_I] > a[a_I]:
            c.append(b[b_I])
            b_I += 1
        elif a[a_I] == b[b_I]:
            if len(a) < len(b):
                a_I += 1
            else:
                b_I += 1

    return c


print(commons(a, b))
