import sys
while True:
    a=sys.stdin.readline().strip()
    if a=="#":break
    j=0
    for i in range(len(a)):
        if a[i] in ["a","e","i","o","u"]:j=i;break
    print(a[j:]+a[0:j]+"ay")