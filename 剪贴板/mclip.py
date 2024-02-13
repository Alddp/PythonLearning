# %%
#! python3
# mclip.py - A multi-clipboard program.

import pyperclip
import sys
TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

# %% [markdown]
# 令行参数将存储在变量sys.argv 中

# %%


if len(sys.argv) < 2:

    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()


keyphrase = sys.argv[1]  # first command line arg is the keyphrase


# %% [markdown]
# 如果keyphrase在字典中,则将值复制到剪贴板

# %%

if keyphrase in TEXT:

    pyperclip.copy(TEXT[keyphrase])

    print("Text for " + keyphrase + " copied to clipboard.")


else:

    print("There is no text for " + keyphrase)

# %%
