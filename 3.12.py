def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result


def main():
    try:
        number = int(input("请输入一个数:\n"))
        while number != 1:
            number = collatz(number)
    except ValueError:
        print("你必须输入一个整数")


if __name__ == "__main__":
    main()
