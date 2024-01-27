def a(lines):
    for i in range(lines):
        for j in range(i + 1):
            print("* ", end="")
        print()


def b(lines):
    for i in range(lines):
        for j in range(lines):
            if j < lines - i - 1:
                print(" ", end="")
            else:
                print("* ", end="")
        print()


def c(lines):
    for i in range(lines):
        for j in range(lines - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()


lines = int(input("请输入行数:"))
c(lines=lines)
