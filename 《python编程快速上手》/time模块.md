# 时间处理

## time模块

- time模块使Python程序能够读取系统时钟的当前时间，最常用的函数有`time.time()`和`time.sleep()`。

### time.time()函数

- UNIX纪元：1970年1月1日0点，即协调世界时（UTC）。`time.time()`函数返回自UNIX纪元以来的秒数，返回值是一个浮点值。这个数字称为UNIX“纪元时间戳”。

```python
import time
time.time()
```

- 纪元时间戳可以用于测量一段代码的运行时间。如果在代码块开始时调用`time.time()`，并在结束时再次调用，就可以用第二个时间戳减去第一个，得到这两次调用之间的时间。

```python
import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))
```

- `time.ctime()`函数返回一个关于当前时间的字符串描述。你也可以选择传入由`time.time()`函数返回的自UNIX纪元以来的秒数，以得到一个时间的字符串值。

```python
import time
time.ctime()
thisMoment  =  time.time()
time.ctime(thisMoment)
```

### time.sleep()函数

- 如果需要让程序暂停一下，就调用`time.sleep()`函数，并传入希望程序暂停的秒数。

```python
import time

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

time.sleep(5)
```

## 数字四舍五入

- 在处理时间时，你经常会遇到小数点后有许多数字的浮点值。为了让这些值更易于处理，可以用Python内置的`round()`函数将它们缩短，该函数按照指定的精度四舍五入一个浮点数。只要传入要处理的数字，再加上可选的第二个参数，指明需要传入小数点后多少位即可。如果省略第二个参数，`round()`会将数字四舍五入到最接近的整数。

```python
import time

now = time.time()
round(now, 2)
round(now, 4)
round(now)
```

## 项目：超级秒表

- 该项目主要利用`time.time()`函数记录每次单圈的开始和结束时间，以此来计算每一圈以及总的运行时间。当用户按下Ctrl-C快捷键时，程序会捕获到`KeyboardInterrupt`异常并优雅地退出。

```python
import time

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
```

## 小结

- 时间处理是编程中常见的任务，Python的`time`模块提供了一些基础但强大的函数来进行时间处理。
- `time.time()`函数可以获取当前的时间戳，`time.sleep()`函数可以使程序暂停指定的秒数。
- `round()`函数可以进行四舍五入操作，使得浮点数的显示更加友好。
- 通过记录和计算时间戳，我们可以轻松地制作出秒表等计时工具。