# %%
import pyperclip
import sys

TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

# %%
if len(sys.argv) < 2:
    print("未传参数")
    sys.exit()

# %%
keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"{keyphrase}短语已经复制到剪贴板")
else:
    print("找不到对应短语")

# %%
