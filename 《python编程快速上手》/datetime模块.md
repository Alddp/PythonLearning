# Python的datetime模块

## datetime数据类型

- `datetime`模块有自己的`datetime`数据类型，`datetime`值表示一个特定的时刻。

```python
import datetime

# 获取当前时间
now = datetime.datetime.now()

# 创建一个特定时间
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)

# 获取年、月、日、时、分、秒
year, month, day = dt.year, dt.month, dt.day
hour, minute, second = dt.hour, dt.minute, dt.second
```

- `datetime.datetime.fromtimestamp()`方法可以将UNIX纪元时间戳转换为`datetime`对象。

```python
import datetime, time

# 将UNIX纪元时间戳转换为datetime对象
dt = datetime.datetime.fromtimestamp(1000000)

# 获取当前时间的datetime对象
now = datetime.datetime.fromtimestamp(time.time())
```

- `datetime`对象可以用比较操作符进行比较。

```python
import datetime

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

# 比较datetime对象
print(halloween2019 == oct31_2019)  # True
print(halloween2019 > newyears2020)  # False
print(newyears2020 > halloween2019)  # True
print(newyears2020 != oct31_2019)  # True
```

## timedelta数据类型

- `datetime`模块还提供了`timedelta`数据类型，它表示一个“时段”，而不是一个“时刻”。

```python
import datetime

# 创建一个表示特定时段的timedelta对象
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

# 获取天、秒、微秒
days, seconds, microseconds = delta.days, delta.seconds, delta.microseconds

# 获取总秒数
total_seconds = delta.total_seconds()

# 将timedelta对象转换为字符串
str_delta = str(delta)
```

- `timedelta`对象可以用于对`datetime`值进行“日期运算”。

```python
import datetime

# 获取当前时间
dt = datetime.datetime.now()

# 创建一个表示1000天的timedelta对象
thousandDays = datetime.timedelta(days=1000)

# 计算1000天后的日期
future = dt + thousandDays
```

- `timedelta`对象可以与`datetime`对象或其他`timedelta`对象相加或相减，也可以乘以或除以整数或浮点数。

```python
import datetime

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)

# 进行日期运算
past = oct21st - aboutThirtyYears
far_past = oct21st - (2 * aboutThirtyYears)
```

## 暂停直至特定日期

- 利用`time.sleep()`方法和一个`while`循环，可以让程序暂停一段特定的时间。

```python
import datetime 
import time

halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)

while datetime.datetime.now() < halloween2016:
    time.sleep(1)
```

## 将datetime对象转换为字符串

- 利用`strftime()`方法可以将`datetime`对象显示为字符串。

```python
import datetime

oct21st  = datetime.datetime(2019, 10, 21, 16, 29, 0)

# 将datetime对象转换为字符串
str1 = oct21st.strftime('%Y/%m/%d %H:%M:%S')
str2 = oct21st.strftime('%I:%M %p')
str3 = oct21st.strftime("%B of '%y")
```

## 将字符串转换成datetime对象

- 如果有一个字符串的日期信息，需要将它转换为`datetime`对象，就用`datetime.datetime.strptime()`函数。

```python
import datetime

# 将字符串转换为datetime对象
dt1 = datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
dt2 = datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
dt3 = datetime.datetime.strptime("October of '19", "%B of '%y")
dt4 = datetime.datetime.strptime("November of '63", "%B of '%y")
```

## 表格：strftime指令

| strftime指令 | 含义                                       |
| ------------ | ------------------------------------------ |
| %Y           | 带世纪的年份，例如'2014'                   |
| %y           | 不带世纪的年份，'00' 至'99' （1970至2069） |
| %m           | 数字表示的月份, '01' 至'12'                |
| %B           | 完整的月份，例如'November'                 |
| %b           | 简写的月份，例如'Nov'                      |
| %d           | 一月中的第几天，'01' 至'31'                |
| %j           | 一年中的第几天，'001' 至'366'              |
| %w           | 一周中的第几天，'0' （周日）至'6' （周六） |
| %A           | 完整的周几，例如'Monday'                   |
| %a           | 简写的周几，例如'Mon'                      |
| %H           | 小时（24小时时钟），'00' 至'23'            |
| %I           | 小时（12小时时钟），'01' 至'12'            |
| %M           | 分，'00' 至'59'                            |
| %S           | 秒，'00' 至'59'                            |
| %p           | 'AM' 或'PM'                                |
| %%           | 就是'%' 字符                               |