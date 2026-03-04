# Josue VillaBonilla
# 3/3/2026
# Travel Expenses Program
# This program calculates and displays travel expenses and remaining budget.


"""
PSEUDOCODE

1. Display program title.
2. Ask user to enter their budget.
3. Ask user to enter travel destination.
4. Ask user how much they will spend on gas.
5. Ask user how much they will spend on accommodation.
6. Ask user how much they will spend on food.
7. Add all expenses together.
8. Subtract total expenses from budget.
9. Display formatted travel expense summary.

"""

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)

print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)

print("\nRemaining Balance:", remaining_balance)
