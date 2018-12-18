import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

pass_len = int(input("How long would you like your password to be? "))

password = "".join(random.sample(s, pass_len))

print(f"Your new password is : {password}")
