import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()_-+~`{}[]|/.,;:"

all_char = lower+upper+number+symbol
length = int(input("Enter the length:"))

password = ''.join(random.sample(all_char,length))
print("General password:",password)