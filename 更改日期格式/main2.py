import os
import re
import shutil

# 创建一个匹配美国日期格式的正则表达式 (MM-DD-YYYY)
date_pattern = re.compile(
    r"""^(.*?) # 所有文本到日期开始
    ((0|1)?\d)-                     # 月份
    ((0|1|2|3)?\d)-                 # 日期
    ((19|20)\d\d)                   # 年份
    (.*?)$                          # 日期结束到所有文本
    """,
    re.VERBOSE,
)

# 遍历工作目录中的所有文件
for amer_filename in os.listdir("."):
    mo = date_pattern.search(amer_filename)

    # 跳过没有日期的文件
    if mo == None:
        continue

    # 获取美国日期格式的各部分
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    # 格式化为欧洲日期格式 (DD-MM-YYYY)
    euro_filename = (
        before_part + day_part + "-" + month_part + "-" + year_part + after_part
    )

    # 获取完整的、绝对文件路径
    abs_working_dir = os.path.abspath(".")
    amer_filename = os.path.join(abs_working_dir, amer_filename)
    euro_filename = os.path.join(abs_working_dir, euro_filename)

    # 重命名文件
    print(f'Renaming "{amer_filename}" to "{euro_filename}"...')
    shutil.move(amer_filename, euro_filename)
