import os
import random


# 生成符合美国日期格式的文件名
def generate_american_date_filename():
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # 为简单起见，将日期限制在28天以内
    year = random.randint(2000, 2025)
    return f"file-{month:02d}-{day:02d}-{year}.txt"


# 生成不符合美国日期格式的文件名
def generate_non_american_date_filename():
    prefixes = ["report", "memo", "presentation", "notes", "budget"]
    suffixes = [".txt", ".docx", ".xlsx", ".pptx"]
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return f"{prefix}-{random.randint(1, 12)}-{random.randint(1, 28)}-{random.randint(2000, 2025)}{suffix}"


# 创建测试文件
def create_test_files(num_files, directory):
    os.makedirs(directory, exist_ok=True)
    for i in range(num_files):
        choice = random.randint(
            1, 4
        )  # 1: 符合美国日期格式的文件名，2: 不符合美国日期格式的文件名，3: 特殊情况，4: 随机选择
        if choice == 1:
            filename = generate_american_date_filename()
        elif choice == 2:
            filename = generate_non_american_date_filename()
        else:
            special_cases = [
                "no-date-here.txt",
                "2023-01-15-report.docx",
                "02-14-2024-love_letter.txt",
            ]
            filename = random.choice(special_cases)
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as file:
            file.write("This is a test file.")


if __name__ == "__main__":
    num_files = 20  # 生成的文件数量
    output_directory = "test_files"  # 测试文件保存的目录

    create_test_files(num_files, output_directory)
    print(f"{num_files} 个测试文件已生成并保存到 {output_directory} 目录中。")
