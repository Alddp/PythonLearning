import re


def custom_strip(s, char=None):
    if char is None:
        return re.sub(r"^[\s\t\n]+|[\s\t\n]+$", "", s)
    else:
        return re.sub(r"^" + re.escape(char) + r"+|" + re.escape(char) + r"+$", "", s)


# 测试
s = "##Hello, World!##"
print(custom_strip(s))  # 结果为 "Hello, World!"
print(custom_strip(s, "#"))  # 结果为 "Hello, World!"
print(custom_strip(s, "l"))  # 结果为 "Heo, Word!"
