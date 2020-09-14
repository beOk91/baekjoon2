while True:
    text=input().lower()
    if text=="#":break
    cnt=0
    for element in text:
        if element in ["a","e","i","o","u"]:cnt+=1
    print(cnt)
