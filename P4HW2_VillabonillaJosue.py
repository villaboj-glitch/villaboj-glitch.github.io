# Josue VillaBonila
# 16 APR 26
# P4HW2 Salary
# This program calculates pay for multiple employees, including overtime pay,
# and displays totals for overtime pay, regular pay, gross pay, and employees entered.

# Pseudocode:
# Ask user for employee name or "Done" to terminate
# Set total overtime pay, total regular pay, total gross pay, and employee count to 0
# While employee name is not "Done"
#     Ask user for number of hours worked
#     Ask user for pay rate
#     If hours worked is more than 40, calculate overtime hours
#     Calculate overtime pay
#     Calculate regular pay
#     Calculate gross pay
#     Add values to totals
#     Add 1 to employee count
#     Display employee pay information
#     Ask for another employee name or "Done"
# Display final totals

employee_name = input('Enter employee\'s name or "Done" to terminate: ')

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while employee_name != "Done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_hours_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_hours_pay = hours_worked * pay_rate

    gross_pay = regular_hours_pay + overtime_pay

    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_hours_pay
    total_gross_pay = total_gross_pay + gross_pay
    employee_count = employee_count + 1

    print()
    print("Employee name:   ", employee_name)
    print()
    print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:.1f}            {pay_rate:.2f}        {overtime_hours:.1f}         ${overtime_pay:.2f}         ${regular_hours_pay:.2f}       ${gross_pay:.2f}")
    print()

    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")