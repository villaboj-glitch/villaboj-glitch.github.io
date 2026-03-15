# Josue VillaBonilla
# 15 MAR 26
# P2HW2 - List Statistics
# This program stores module grades in a list and displays
# the lowest grade, highest grade, sum of grades, and average.

"""
Pseudocode:
1. Ask the user to enter the grade for Module 1.
2. Ask the user to enter the grade for Module 2.
3. Ask the user to enter the grade for Module 3.
4. Ask the user to enter the grade for Module 4.
5. Ask the user to enter the grade for Module 5.
6. Ask the user to enter the grade for Module 6.
7. Store all six grades in a list named module_grades.
8. Find the lowest grade in the list.
9. Find the highest grade in the list.
10. Find the sum of the grades in the list.
11. Find the average by dividing the sum by the number of grades.
12. Display the results in the required format.
"""

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

module_grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

print()
print("--------------Results--------------")
print(f"{'Lowest Grade:':<22}{lowest_grade:.1f}")
print(f"{'Highest Grade:':<22}{highest_grade:.1f}")
print(f"{'Sum of Grades:':<22}{sum_of_grades:.1f}")
print(f"{'Average:':<22}{average_grade:.2f}")
print("-----------------------------------")