n=int(input())
for _ in range(n):
    text=input()
    arr=[0]*26
    for element in text:
        if element.isalpha():
            arr[ord(element)-97]+=1
    print(chr(arr.index(max(arr))+97) if arr.count(max(arr))==1 else "?")