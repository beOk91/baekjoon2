while True:
    text=input().lower()
    if text=="#":break
    arr=[False]*26
    for element in text:
        if element.isalpha():arr[ord(element)-97]=True
    print(sum(1 if arr[i] else 0 for i in range(26)))