usr_nmbr = int(input("Which number do you want divisors of? >> "))

for i in range(1, usr_nmbr):
    if usr_nmbr % i == 0:
        print(i)

