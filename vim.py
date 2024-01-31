def triangle(line):
    for i in range(line):
        for j in range(i + 1):
            print("* ", end="")
        print()


def multiplication_table():
    rows = 9  # 乘法表的行数
    # 外层循环控制行数
    for i in range(1, rows + 1):
        # 内层循环控制每行中的列数
        for j in range(1, i + 1):
            # 打印乘法表达式并进行对齐
            print(f"{j} × {i} = {j*i:2d}\t", end="")
        print()  # 换行


def triangle_2(line):
    for i in range(line):
        for _ in range(line - i - 1):
            print("  ", end="")
        for _ in range(i):
            print(" *", end="")
        print()


def triangle_3(line):
    for i in range(line):
        for _ in range(line - i - 1):
            print(" ", end="")
        for _ in range(i):
            print(" *", end="")
        print()


if __name__ == "__main__":
    line = 5
    triangle(line=line)
    triangle_2(line=line)
    triangle_3(line=line)
    multiplication_table()
