# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:18:53 2022

@author: mmacarty
"""

TAX_RATE = .20
STANDARD_DEDUCTION = 12200
DEPENDENT_DEDUCTION = 2000

income = float(input("Enter your income: "))
dependents = int(input("Enter number dependents: "))

taxable_income = income - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * dependents

income_tax_due = taxable_income * TAX_RATE
income_tax_due = f"${income_tax_due:,.2f}"
taxable_income = f"${taxable_income:,.2f}"



# print("Your taxable income is:", taxable_income)
# print("Your taxable income is:", "$" + str(taxable_income))
# print("Your taxable income is: $%.2f" % taxable_income)
# print("Your taxable income is: ${}".format(taxable_income))
print(f"{'Your taxable income is':30s} {taxable_income:>12}")
print(f"{'Income tax due is':30s} {income_tax_due:>12}")