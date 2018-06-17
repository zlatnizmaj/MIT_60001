# -*- coding: utf-8 -*-
"""
Assignments MIT6_0001
ps1
    ps1a.py

@author: Nguyễn Phương Nam _KHMT K28
"""
annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary / 12

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
monthly_saving = monthly_salary * portion_saved

total_cost = float(input("Enter the cost of your dream house: "))
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

r = 0.04 # annual return

current_saving = 0
number_of_month = 0
print(monthly_saving)
print(down_payment)
while (current_saving < down_payment):
    curent_saving_with_annual_return = current_saving * r /12
    print(curent_saving_with_annual_return)
    current_saving += monthly_saving + curent_saving_with_annual_return
    print(current_saving)
    number_of_month += 1
    
print(f"Number of months: {number_of_month}")