user_input = input("Enter a number: ")

try: 
    number = int(user_input)
    print(f'Number you entered: {number}')
except ValueError:
    print("Try with an integer")
except Exception:
    print("Something went wrong")
    