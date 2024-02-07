# %%
"""
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

# %% [markdown]
# 1．从剪贴板粘贴文本。

# %%
import pyperclip

text = pyperclip.paste()

# %% [markdown]
# 2. 处理文本

# %%
# 分隔行
lines = text.split("\n")

for i in range(len(lines)):
    lines[i] = "*" + lines[i]

text = "\n".join(lines)
