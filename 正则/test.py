import re


def is_valid_date(day, month, year):
    # 检查闰年
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 检查月份天数是否有效
    if day > days_in_month[month - 1]:
        return False

    return True


# 正则表达式匹配日期
pattern = re.compile(
    r"""\b(0[1-9]|[12]\d|3[01])\/(0[1-9]|1[0-2])\/((1[0-9]{3})|2[0-9]{3})\b""",
    re.VERBOSE,
)

# 测试日期
test_dates = ["31/02/2020", "29/02/2021", "31/04/2021"]

for date in test_dates:
    match = pattern.match(date)
    if match:
        day, month, year = map(int, match.groups())
        if is_valid_date(day, month, year):
            print(f"{date} is a valid date.")
        else:
            print(f"{date} is not a valid date.")
    else:
        print(f"{date} does not match the date pattern.")
