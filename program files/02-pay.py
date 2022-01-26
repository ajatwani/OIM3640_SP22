# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:50:31 2022

@author: mmacarty


"""

WEEKS = 50


wage = float(input("Enter hourly wage:\n"))
week_hours = int(input("How many hours per week? "))

pay_weekly = wage * week_hours
# annual pay is 50 * weekly
pay_annual = pay_weekly * WEEKS
pay_monthly = pay_annual / 12

print(f"Weekly pay: {pay_weekly}")
print(f"Monthly pay: {pay_monthly}")
print(f"Annual pay: {pay_annual}")
