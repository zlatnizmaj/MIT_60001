# -*- coding: utf-8 -*-
"""
Assignments MIT6_0001
ps1
    ps1a.py

@author: Nguyễn Phương Nam _KHMT K28
"""
import os

answer = "y"
while (answer != "n" and answer != "N"):
    unused_variable_answer = os.system("cls")
    
    while True:
        try:
            annual_salary = float(input("Enter your annual salary: "))
            portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
            break
        except:
            print("Plz enter NUMBER!!!")
    
    monthly_salary = annual_salary / 12
    
    answer = str(input("Do you want to continue? (y/n): "))
    if (answer == "n" or answer == "N"):
        print("\n Thank you and see you again! :-)")
        break

