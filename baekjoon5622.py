text=input().strip()
time=0
for i in range(len(text)):
    if text[i] in ["S","V"]:
        temp=ord(text[i])-66
    elif text[i] in ["Y","Z"]:
        temp=ord(text[i])-67
    else:
        temp=ord(text[i])-65
    time+=(temp//3+3)
print(time)