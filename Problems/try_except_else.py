#

while True:
    try:
        value1 = int(input("enter value 1: "))
        value2 = int(input("enter value 2: "))
        # break
    except:
        print("input correct value")
    else:
        break

try:
    result1 = value1 / value2
    print(result1)
except ZeroDivisionError:
    print("cannot be zero")
except:
    print("something wrong")
finally:
    print("result")
    # print(result1)
