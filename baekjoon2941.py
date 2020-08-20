import sys
text=sys.stdin.readline().strip()
croatia_text=["c=","c-","dz=","d-","lj","nj","s=","z="]
for element in croatia_text:
    text=text.replace(element,'a')
print(len(text))