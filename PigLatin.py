# 打印提示信息
print("Enter  the  English  message  to  translate  into  Pig  Latin:")
# 获取用户输入的英文消息
message = input()

# 定义元音字母
VOWELS = ("a", "e", "i", "o", "u", "y")

# 创建一个空列表，用于存储转换后的 Pig Latin 消息
pigLatin = []
# 遍历用户输入的每一个单词
for word in message.split():
    # 创建一个空字符串，用于存储单词的前缀非字母
    prefixNonLetters = ""
    # 当单词长度大于0，且第一个字母不是字母时，循环执行以下操作
    while len(word) > 0 and not word[0].isalpha():
        # 将单词的第一个字母添加到前缀非字母字符串中
        prefixNonLetters += word[0]
        # 将单词的第一个字母从原单词中移除
        word = word[1:]
    # 如果原单词长度为0，则直接将前缀非字母字符串添加到 pigLatin 列表中，并跳过本次循环
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # 创建一个空字符串，用于存储单词的后缀非字母
    suffixNonLetters = ""
    # 当单词的最后一个字母不是字母时，循环执行以下操作
    while not word[-1].isalpha():
        # 将单词的最后一个字母添加到后缀非字母字符串中
        suffixNonLetters += word[-1]
        # 将单词的最后一个字母从原单词中移除
        word = word[:-1]

    # 创建一个布尔变量，用于存储原单词是否为大写字母
    wasUpper = word.isupper()
    # 创建一个布尔变量，用于存储原单词是否为标题字母
    wasTitle = word.istitle()

    # 将原单词转换为小写字母
    word = word.lower()

    # 创建一个空字符串，用于存储单词的前缀辅音
    prefixConsonants = ""
    # 当单词长度大于0，且第一个字母不是元音字母时，循环执行以下操作
    while len(word) > 0 and not word[0] in VOWELS:
        # 将单词的第一个字母添加到前缀辅音字符串中
        prefixConsonants += word[0]
        # 将单词的第一个字母从原单词中移除
        word = word[1:]

    # 如果前缀辅音字符串不为空，则将前缀辅音字符串添加到原单词的末尾，并添加 "ay"
    if prefixConsonants != "":
        word += prefixConsonants + "ay"
    # 否则，直接将 "yay" 添加到原单词的末尾
    else:
        word += "yay"

    # 如果原单词为大写字母，则将转换后的单词转换为大写字母
    if wasUpper:
        word = word.upper()
    # 如果原单词为标题字母，则将转换后的单词转换为标题字母
    if wasTitle:
        word = word.title()

    # 将转换后的单词添加到 pigLatin 列表中
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# 将 pigLatin 列表中的每一个单词用空格连接起来，并打印出来
print(" ".join(pigLatin))
