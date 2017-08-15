import time


def is_valid_date(str):
    try:
        time.strptime(str, "%Y-%m-%d")
        return True
    except:
        return False


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True  # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True  # 非整百年能被4整除的为闰年
    else:
        return False


def caculate_day(str):
    date_split = str.split('-')  # ['2017','06','15']
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    year = int(date_split[0])
    month = int(date_split[1])
    day = int(date_split[2])

    if ((month >= 3) and (is_leap_year(year))):
        noDay = months[month - 1] + day + 1
    else:
        noDay = months[month - 1] + day
    return noDay


while True:
    date = input("Please input the Date as YYYY-MM-DD(e.g.: 2017-06-15):")
    if date == "exit":
        break

    try:
        if is_valid_date(date):
            noDay = caculate_day(date)
            print("It's the %s day of the year" % noDay)
        else:
            print('Invalid date')
    except:
        pass
