text=input()
result=10
for i in range(1,len(text)):
    result=result+10 if text[i-1]!=text[i] else result +5
print(result)