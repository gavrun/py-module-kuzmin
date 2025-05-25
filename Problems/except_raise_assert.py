#

value1 = int(input("enter value 1: "))
value2 = int(input("enter value 2: "))

result = value1 / value2
print(result)

#

value3 = int(input("enter value 1: "))
value4 = int(input("enter value 2: "))

if value4 == "0":
    raise Exception("cannot be zero")

result2 = value3 / value4
print(result2)

#

value5 = int(input("enter value 1: "))
value6 = int(input("enter value 2: "))

assert(value6 != "0"), "cannot be zero"

result3 = value5 / value6
print(result3)

#

while True:
    try:
        value5 = int(input("enter value 1: "))
        value6 = int(input("enter value 2: "))
        break
    except:
        print("input correct value")

try:
    result3 = value5 / value6
    print(result3)
except:
    print("something wrong")
