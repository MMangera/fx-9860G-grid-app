import os
import gridapp as g
a = input("Folder name? (file(s) must be in folder to load)")
b = input("File extension? (add '.' at start, e.g. '.txt')")
c = input("Info:\n\nYou need to call the files in the folder as 'file' followed by the index of the file, e.g. 'file1'. If this is not so the program will not work.\nContinue? (y/n)")
if c.lower == 'n':
    raise KeyboardInterrupt("user stopped control flow")
path = os.path.abspath(__file__)
idx = 1
read = []
while True:
    try:
        f = open(path[:-19]+f"{a}/file{idx}{b}", "r")
        read += [i[9:].strip() for i in f.readlines()]
        f.close()
    except FileNotFoundError:
        break
    idx += 1
ans = []
for i in read:
    try:
        ans.append(list(eval(i)))
    except Exception:
        continue
g.main(load=ans)
