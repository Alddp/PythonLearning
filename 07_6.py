def main():
    num = 8
    list = [[]] * num
    # 第一列都为1
    for row in range(num):
        # 初始化
        list[row] = [None] * (row + 1)
        for inner in range(len(list[row])):
            if inner == 0 or inner == row:
                list[row][inner] = 1
            else:
                list[row][inner] = list[row - 1][inner - 1] + list[row - 1][inner]
            print(list[row][inner], end="\t")
        print()


if __name__ == "__main__":
    main()
