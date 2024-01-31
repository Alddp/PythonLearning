import pprint

string = (
    "Hello everyone, I am a student form china, currantly learning in Zhangzhou school"
)
json = {}
for character in string:
    json.setdefault(character, 0)
    json[character] = json[character] + 1
pprint.pprint(json)


print("hello world")
for i in range(20):
    print("hello world")
