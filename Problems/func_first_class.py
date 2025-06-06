# test the performance of other functions with First-Class Functions

import datetime

def my_function(a, b):
    return a + b

start = datetime.datetime.now()
my_function(10, 4)
end = datetime.datetime.now()

total_time = end - start
print(total_time)

#

def test_function(func, *args):
    start = datetime.datetime.now()
    func(*args)
    end = datetime.datetime.now()
    total_time = end - start
    print(total_time)

def my_function(a, b):
    return a + b

test_function(my_function, 10, 4)

#

def test_function(number_of_times, func, *args):
    accumulated_time = datetime.timedelta()
    for x in range(number_of_times):
        start = datetime.datetime.now()
        func(*args)
        end = datetime.datetime.now()
        total_time = end - start
        accumulated_time += total_time

    avg_time = accumulated_time / number_of_times
    print(avg_time)

def my_function(a, b):
    return a + b

test_function(my_function, 10, 4)
