import emoji
from math import sqrt

number = float(input("Enter a number: "))
root = sqrt(number)
print(emoji.emojize(f"The square root ::hash:: of {number:.2f} is {root:.2f}", language='alias'))