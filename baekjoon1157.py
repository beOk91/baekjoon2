text=input().upper()
arr=[0]*26
for element in text:
    arr[ord(element)-65]+=1
maxIndex,maxCnt=0,0

for i in range(0,26):
    if i!=0 and arr[maxIndex]<arr[i]:
        maxIndex=i
    if max(arr)==arr[i]:
        maxCnt+=1
print("?" if maxCnt>1 else chr(maxIndex+65))