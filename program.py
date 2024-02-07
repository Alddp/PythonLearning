#! python3
# mclip.py - A multi-clipboard program.

# 定义一个字典，用于存储文本
TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

# 导入sys模块和pyperclip模块
import sys, pyperclip

# 如果命令行参数小于2，则打印提示信息并退出
if len(sys.argv) < 2:
    print("Usage: py mclip.py [keyphrase] - copy phrase text")
    sys.exit()

# 将命令行参数赋值给keyphrase
keyphrase = sys.argv[1]

# 如果keyphrase在TEXT字典中，则将TEXT字典中对应的文本复制到剪贴板，并打印提示信息
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
# 否则，打印提示信息
else:
    print("There is no text for " + keyphrase)
