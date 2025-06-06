# decorator 

import time


def select(input_func):    
    def output_func():
        print("*****************")
        input_func()
        print("*****************")
    return output_func

@select
def hello():
    print("***something else***")

hello()

#

def perf_test(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        finish = time.perf_counter()
        performance = finish - start
        print(f'Exec time: {performance} ')
    return wrapper

@perf_test
def print_numbers(num):
    for i in range(0, num):
        print(i)

print_numbers(10)

