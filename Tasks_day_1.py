"""Day 1: Division and Square-root
Write a function called divide_or_square that takes one argument (a number),
and returns the square root of the number if it is divisible by 5,
returns its remainder if it is not divisible by 5. For example,
if you pass 10 as an argument,
then your function should return 3.16 as the square root."""
import math
print("Hello, Lets me check you number")
number=int(input("Please add you number  "))
if number%5==0:
    sqrt_number=math.sqrt(number)
    print(f"Number can divide and squarte root {sqrt_number}")
elif number%5!=0:
    new_number=number%5
    print(f"You number divide other part {new_number}")
else:
    print("Please add real number.")