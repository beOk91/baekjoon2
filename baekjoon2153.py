text=input().strip()
result,cnt=0,0
for element in text:
    if element.islower():result+=ord(element)-(97-1)
    else:result+=ord(element)-(65-27)
for i in range(1,result+1):
    if result%i==0:cnt+=1
print("It is a prime word." if cnt==2 or cnt==1 else "It is not a prime word.")