import json
from collections import OrderedDict

# 读取settings.json文件
with open(
    "D:/Destok/MyGit/PythonLearning/jsonFormate/b.json", "r", encoding="utf-8"
) as f:
    data = json.load(f, object_pairs_hook=OrderedDict)

# 按键名排序
sorted_data = OrderedDict(sorted(data.items()))

# 将结果写回文件
with open(
    "D:/Destok/MyGit/PythonLearning/jsonFormate/c.json", "w", encoding="utf-8"
) as f:
    json.dump(sorted_data, f, indent=4)
