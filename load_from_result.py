import os
import gridapp as g
a = input("Folder name? (file(s) must be in folder to load)")
path = os.path.abspath(__file__)
idx = 1
read = []
while True:
    try:
        f = open(path[:-7]+f"{a}/scam{idx}.py", "r")
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