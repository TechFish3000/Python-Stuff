# DayoftheWeek v 1.2
# Created by TechFish3000
# Last revision on 24 May, 2019, 8:56 am

# Program to get the day of the week for any given date.
# https://en.wikipedia.org/wiki/Zeller's_congruence
# Formula is (q + ((13(m + 1)) // 5) + K + (K // 4) + (J // 4) - 2J) mod 7

leapyear = 'n'

def date2dotw(day, month, year): # define function

    global leapyear
    yearproof = year
    if month == 1:
        actual_month = 13  # set mathematical constant for month to 13, january
        year = year - 1  # for the equation, it is part of the year before
    elif month == 2:
        actual_month = 14  # set mathematical constant for month to 14, february
        year = year - 1  # for the equation, it is part of the year before
    else:
        actual_month = month  # if it is not january or february, don't mess with it
    year_last_2_num = year % 100   # get the last 2 numbers of the year
    year_first_2_num = year // 100  # and the first two

    step_1 = 13 * (actual_month + 1)  # 13(m + 1)
    step_1point5 = step_1 // 5  # step1 floordiv 5
    step_2 = year_last_2_num // 4  # Last two numbers floordiv by 4
    step_3 = year_first_2_num // 4 # first two numbers floordiv by 4
    step_4 = 2 * year_first_2_num  # First two num * 2
    step_5 = day + step_1point5 + year_last_2_num + step_2 + step_3 - step_4  # finish formula
    end_result = step_5 % 7 # mod 7
    if day == 29 and month == 2:  # if it tries to say it's a leap year
        if yearproof % 4 == 0:  # if it actually is, disregard
            leapyear = "y"
        else:                   # if not, invalid
            leapyear = "i"

    if end_result == 0:        # return tree for values
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Saturday'
    elif end_result == 1:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Sunday'
    elif end_result == 2:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Monday'
    elif end_result == 3:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Tuesday'
    elif end_result == 4:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Wednesday'
    elif end_result == 5:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Thursday'
    elif end_result == 6:
        if leapyear == 'i':
            return 'Invalid'
        else:
            return 'Friday'


# Examples

print(date2dotw(23, 5, 2019))
print(date2dotw(1, 1, 1900))
print(date2dotw(31, 12, 2000))
print(date2dotw(29, 2, 2020))
print(date2dotw(31, 10, 1752))
print(date2dotw(30, 6, 1896))
print(date2dotw(1, 1, 1))
print(date2dotw(29, 2, 2018))

