# TDD step 1

# class Calculator:
#     def adding(self, a, b):
#         pass

#     def dividing(self, a, b):
#         pass

# TDD step 2

class Calculator:
    def adding(self, a, b):
        return a + b

    def dividing(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    print("Simple calculator")
    print("2 + 3 =", calc.adding(2, 3))
    print("10 / 2 =", calc.dividing(10, 2))

    try:
        print("10 / 0 =", calc.dividing(10, 0))
    except ZeroDivisionError:
        print("Caught division by zero")
