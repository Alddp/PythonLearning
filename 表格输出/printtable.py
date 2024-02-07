tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printtable(tableData):

    colwidths = [0] * len(tableData)

    for i in range(len(tableData)):
        max_width = 0
        for j in tableData[i]:
            if max_width < len(j):
                max_width = len(j)
        colwidths[i] = max_width

    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            content = tableData[j][i]
            if j == 0:
                content = content.rjust(colwidths[j])
            else:
                content = content.ljust(colwidths[j])
            print(content, end=" ")
        print()


printtable(tableData=tableData)
