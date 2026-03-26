# Josue VillaBonilla
# 26 MAR 26
# P3LAB
# This program breaks a money amount into the fewest number of
# dollars, quarters, dimes, nickels, and pennies.

amount = float(input("Enter the amount of money as a float: $"))

total_cents = int(round(amount * 100))

if total_cents == 0:
    print("No change")
else:
    dollars = total_cents // 100
    total_cents = total_cents - (dollars * 100)

    quarters = total_cents // 25
    total_cents = total_cents - (quarters * 25)

    dimes = total_cents // 10
    total_cents = total_cents - (dimes * 10)

    nickels = total_cents // 5
    total_cents = total_cents - (nickels * 5)

    pennies = total_cents

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")