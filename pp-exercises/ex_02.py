usr_input = int(input("Pick a number: >> "))
check_by = int(input("Choose a number to devide by: >> "))


if usr_input % 4 == 0:
    print("Number divisible by 4...")
elif usr_input % 2 == 0:
    print("Number divisible by 2...")
else:
    print("Number is odd...")

if usr_input % check_by == 0:
    print(f"Divides evenly by {check_by}")
else:
    print(f"Does not divide evenly by {check_by}")
