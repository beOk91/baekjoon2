import sys
text=sys.stdin.readline().strip()
for i in ["a","e","i","o","u"]:
    text=text.replace(i+"p"+i,i)
print(text)