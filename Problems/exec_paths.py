# check all execution paths

temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    prin("Below zero") # <-- prin() stays hidden
else:
    print("Zero")

