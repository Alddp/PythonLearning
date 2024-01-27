from math import sqrt

# 输入一个正整数判断是不是素数。
num = int(input("请输入一个正整数:"))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if end % x == 0:
        is_prime = False
        break

if is_prime == True:
    print(f"{num}是素数")
else:
    print(f"{num}不是素数")
