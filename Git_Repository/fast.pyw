# ! python3
# fast.py - quickly open repository from github with cmd
# usage: --> github repositoryname
import sys
import webbrowser

if len(sys.argv) < 2:
    # print("请输入参数")
    sys.exit()

url = "https://github.com/Alddp/" + sys.argv[1]

# TODO: open webbrowser
webbrowser.open(url)
