from random import randint

lt = int(input("What number should be the max? >> "))

a_list = [i for i in range(randint(lt, 100))]

print([i for i in a_list if i < lt])
