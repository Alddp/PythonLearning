import re


def is_strong_password(password):
    # 长度至少为8个字符
    if len(password) < 8:
        return False

    # 至少包含一个大写字母
    if not re.search(r"[A-Z]", password):
        return False

    # 至少包含一个小写字母
    if not re.search(r"[a-z]", password):
        return False

    # 至少包含一个数字
    if not re.search(r"\d", password):
        return False

    return True


# 测试密码
test_passwords = ["12345678", "abcdefg", "ABCDEFG", "abcdefg1", "ABCDEFG1"]

for password in test_passwords:
    if is_strong_password(password):
        print(f"{password} is a strong password.")
    else:
        print(f"{password} is not a strong password.")
