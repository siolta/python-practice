message = input("What would you like me to echo? >  ")

count = input("And how many times? >  ")

if len(count) == 0:
    count = 1

def _echo(message, count):
    for i in range(int(count)):
        print(message)

_echo(message, count)
