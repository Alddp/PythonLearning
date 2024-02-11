# 重命名为阿拉伯数字


from pathlib import Path
import re


# 定义一个函数，将中文数字转换为阿拉伯数字
def chinese_to_arabic(chinese_numeral):
    mapping = {
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "十": "10",
        "十一": "11",
        "十二": "12",
        "十三": "13",
        "十四": "14",
        "十五": "15",
        "十六": "16",
        "十七": "17",
        "十八": "18",
        "十九": "19",
        "二十": "20",
    }
    return mapping.get(chinese_numeral, chinese_numeral)


def rename_file(folder: Path, pattern: re.search):

    folder = Path("D:\Destok\《python编程快速上手》")

    # 遍历文件
    for filename in folder.rglob("*"):
        if filename.is_file() and filename.suffix == ".md":
            new_name = (
                re.sub(
                    pattern,
                    lambda m: chinese_to_arabic(m.group(2)),
                    filename.stem,
                )
                + filename.suffix
            )
            filename.replace(new_name)


if __name__ == "__main__":
    partten = re.compile(
        r"""^(.*?)
            第
            ((十)?(一|二|三|四|五|六|七|八|九|十)?)
            章
            (.*?)$
    """,
        re.VERBOSE,
    )
    rename_file(Path("D:/Destok/《python编程快速上手》/"), partten)
