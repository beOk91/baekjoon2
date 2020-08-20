text=input()
arr=[0]*26
for element in text:
    arr[ord(element)-97]+=1
print(" ".join(str(element) for element in arr))