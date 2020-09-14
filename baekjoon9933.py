n=int(input())
pwd_list,result=[],""
for _ in range(n):
    text=input().strip()
    if text[::-1] in pwd_list or text==text[::-1]:result=text
    pwd_list.append(text)
print(len(result),result[len(result)//2])