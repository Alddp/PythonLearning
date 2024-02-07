#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

# 导入pyperclip和re模块
import pyperclip, re

# 创建正则表达式，用于匹配电话号码
phoneRegex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?             # area code
    (\s|-|\.)?                     # separator
    (\d{3})                        # first 3 digits
    (\s|-|\.)                      # separator
    (\d{4})                        # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )""",
    re.VERBOSE,
)

# 创建正则表达式，用于匹配邮箱
# TODO: Create email regex.

# Create email regex.
# 创建正则表达式，用于匹配邮箱
emailRegex = re.compile(
    r"""(
    [a-zA-z0-9.%-_+]+
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )""",
    re.VERBOSE,
)

# TODO: Find matches in clipboard text.
# 查找剪贴板文本中的匹配
# Find matches in clipboard text.
text = str(pyperclip.paste())

# 创建一个空列表，用于存放匹配结果
matches = []
# 使用正则表达式查找电话号码
for groups in phoneRegex.findall(text):
    # 将电话号码拼接成标准格式
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    # 如果存在扩展号，则拼接上扩展号
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    # 将电话号码添加到列表中
    matches.append(phoneNum)
# 使用正则表达式查找邮箱
for groups in emailRegex.findall(text):
    # 将邮箱添加到列表中
    matches.append(groups[0])


# 将匹配结果复制到剪贴板
# Copy results to the clipboard.
if len(matches) > 0:
    # 将匹配结果拼接成字符串，并复制到剪贴板
    pyperclip.copy("\n".join(matches))
    # 打印提示信息
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    # 打印提示信息
    print("No phone numbers or email addresses found.")
