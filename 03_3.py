# 输入三条边长，如果能构成三角形就计算周长和面积。


a = float(input("1:"))
b = float(input("2:"))
c = float(input("3:"))

if a + b > c and a + c > b and b + c > a:
    print("周长为:%f" % (a + b + c))
    p: float = (a + b + c) / 2
    s: float = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("面积:%f" % (s))
else:
    print("无法构成三角形")

