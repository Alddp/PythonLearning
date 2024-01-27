def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("请输入第一个正整数："))
num2 = int(input("请输入第二个正整数："))

gcd_num = gcd(num1, num2)
lcm_num = lcm(num1, num2)

print("两个正整数的最大公约数是：", gcd_num)
print("两个正整数的最小公倍数是：", lcm_num)
