income = float(input("Enter the annual income: "))

income_incents = income * 100 # thalers to cents 
tax_relief_incents = 556 * 100 + 2 

# tax
# evaluate by rule
# < 85,528t tax 18% minus 556t 2c
# > 85,528t tax 14,839t 2c plus 32% of surplus on 85,528t
# never returns money to its citizens
# tax is less than zero, it only means no tax at all

threshold_incents = 85528 * 100

if income_incents <= 0:
    tax_incents = 0
elif income_incents <= threshold_incents:
    tax_incents = (income_incents / 100) * 18 - tax_relief_incents
    if tax_incents < 0:
        tax_incents = 0
else:
    tax_incents = (14839 * 100 + 2) + ((income_incents - threshold_incents) / 100 * 32)

# accept one floating-point value
# tax rounded to full thalers
# print the calculated tax

tax_inthalers = tax_incents / 100 # thalers to cents 
tax_inthalers = round(tax_inthalers, 0)
print("The tax is:", tax_inthalers, "thalers")
