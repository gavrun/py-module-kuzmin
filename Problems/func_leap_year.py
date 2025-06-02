def is_year_leap(year):
    # A leap year, if divided by 4, but not divided into 100,
    # except when it is divided into 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Verification of the correctness of the input data
    if month < 1 or month > 12:
        return None

    # Default months length
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Accounting for the leap year for February
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return month_lengths[month - 1]

def day_of_year(year, month, day):
    # Checking the correctness of the month
    if month < 1 or month > 12:
        return None

    # We get the number of days in the current month
    days_in_current_month = days_in_month(year, month)
    if days_in_current_month is None or day < 1 or day > days_in_current_month:
        return None

    # We summarize the days of the previous months
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    return total_days


# Test 1
test_data = [1900, 2000, 2016, 1987]
test_results1 = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results1[i]:
        print("OK")
    else:
        print("Failed")


# Test 2
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results2 = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results2[i]:
		print("OK")
	else:
		print("Failed")


# Test 3
print(day_of_year(2000, 12, 31))  # 366 (leap year)
print(day_of_year(2001, 12, 31))  # 365 (ordinary year)
print(day_of_year(2024, 2, 29))   # 60 (leap year)
print(day_of_year(2023, 2, 29))   # None (error - February 29 in the innocent year)
print(day_of_year(2023, 13, 1))   # None (the month is incorrect)
print(day_of_year(2023, 4, 31))   # None (only 30 days in April)


