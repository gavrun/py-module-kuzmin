

def fun(obj, index):
    return obj[index]

x = "ABBA"
print(fun(x,3))
# print(fun(x,4)) # IndexError: string index out of range

while True:
    try:
        k = int(input("Enter the index: "))
        f = fun(x,k)
        break
    except ValueError as er:
        print('Attention! ', type(er), er)
    # except IndexError: # Intercepts and processes the exception
    #     print('\nThe index is outside the range')
    finally:
        print('Disconnect power')
    print('End loop')

print(f)

    
