# Package
# When packing arguments, all the presented positional arguments
# will be assembled in a motorcade 'Order', and key - in the dictionary 'Info'
def print_order(*order, **info):
    print("Ваш заказ\n")

    # The dictionary 'Infos' should contain the keys 'Author' and 'Day'
    for key, value in sorted(info.items()):
        print(key, ":", value)

    # Cortege 'Order' contains all the names of the product
    print("Вы выбрали:")
    for item in order:
        print("  -", item)

    print("\nПриходите еще!")



# Calling the function and the transfer of arguments to "packaging"

print_order("Кресло", "Диван", "Стол", "Шкаф", "Стул",
            manager = "Иванов И.И.", day = "07/05/2020")


# Unpacking
abc = [3, 5, 4]
params = dict(print_error=True, units="кв.м.")
# When unpacking arguments, the list of 'ABC' will be unpacked to positional arguments
# Dictionary 'Params' - in named (key)


# The area of ​​the triangle according to the Heron formula
# The function returns the line

def heron_area_str(a, b, c, units="сантиметры", print_error=False):
    if a + b <= c or a + c <= b or b + c <= a:
        if print_error:
            return "Проверьте введенные стороны треугольника!"
        return

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return "\n{} {}".format(s, units)

# Calling the function and transfer of arguments for unpacking

print(heron_area_str(*abc, **params))
