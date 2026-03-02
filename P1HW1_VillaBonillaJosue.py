# Josue VillaBonilla
# 3/1/2026
# P1HW1
# The user should be able to enter any integer for the base value and the exponent. Then print the string showing the base, exponent, and the result.

print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(f"{base} raised to the power of {exponent} is {result} !!")

print()
print("-----Addition and Subtraction-----")

print()
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

total = num1 + num2 - num3

print()
print(f"{num1} + {num2} - {num3} is equal to {total}")