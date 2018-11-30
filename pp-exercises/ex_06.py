user_in = str(input(" > "))

print("It's a palindrome") if user_in == user_in[::-1] else print("Fuck nah")
