a = 10
c = 0

try:
    b = int(input("Enter the denominator: "))
    c = a/b
    print(c)
except ValueError:
    print("The transformation was unsuccessful")
except ZeroDivisionError:
    print("Error - Division into zero")
except:
    print("Error")

print(c)
