import sys
while True:
    text=sys.stdin.readline().strip().lower().split()
    if text[0]=="#":break
    print(text[0],sum(e.count(text[0]) for e in text[1:]))