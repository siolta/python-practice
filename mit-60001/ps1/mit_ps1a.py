#!/usr/bin/env python3

annual_salary = float(input("Enter your annual salary: ​"))
portion_saved = annual_salary / 12 * \
    float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

return_rate = 0.04
portion_down_payment = 0.25
current_savings = 0

total_months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * return_rate / 12
    current_savings += portion_saved
    total_months += 1

print(f"Number of months: {total_months}")
