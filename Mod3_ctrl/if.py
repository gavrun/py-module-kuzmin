# number 1 is logical truth
if 1:
   print("hello 1")
#elif 2:
#    print("hello 2")

lst = [1, 2, 3]
if lst :
   print("hello 4")

# Ternary expression
a = 20
b = "Spring" if a > 10 else "Autumn"
print(b)

# The area of ​​permissible names
trustName=['Ivan', 'Stepan', 'Nikolai']
if 'Stepan' in trustName:
   print('Entered')
else:
   print('Not allowed ')

# Switch replacement using a dictionary
dp = {"min": -50, "dop": 20, "rab": 30, "max": 55}
choice = "dop"
res = dp[choice]
#res = dp.get(choice, "0") # Using the GET method to obtain the default value
print(res)

""" A whole number is given.Determine whether it is even """
a = int(input("Enter a whole number: "))
if a % 2 == 0:
    print("Number", a, "even")
#else:
print("Number" , a, "Not even")

