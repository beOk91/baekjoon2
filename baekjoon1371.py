try:
    arr=[0]*26
    while True:
        text=input()
        for element in text:
            if element >='a' and element<='z':
                arr[ord(element)-97]+=1
except:
    for i in range(len(arr)):
        if arr[i]==max(arr):
            print(chr(i+97),end="")
    exit()