import shelve

shelfFile = shelve.open("./文件操作/mydata")
# cats = ["Zophie", "Pooka", "Simon"]
# shelfFile["cats"] = cats
shelfFile["cats"]
shelfFile.close()
