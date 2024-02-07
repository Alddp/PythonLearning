def s1(row):
    for i in range(row):
        print("* " * i, end="\n")


def s2(row):
    for i in range(row):
        for j in range(row - 1 - i, 0, -1):
            print("  ", end="")

        for k in range(i):
            print(" *", end="")
        print()


def s2(row):
    for i in range(row):
        print("  " * (row - i - 1), end="")
        print(" *" * i, end="")
        print()


s2(5)


def s3(row):
    for i in range(row):
        for _ in range(row - i):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()


def s3(row):
    for i in range(row):
        print(" " * (row - i), end="")
        print("*" * (2 * i + 1), end="")
        print()


s3(2)
