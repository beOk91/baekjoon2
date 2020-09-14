text=input().strip().split()
a,b=text[0],"".join(i for i in text[1:])
for i in range(len(text)):
    if i==0:print(text[i].upper()[0],end="")
    elif text[i] in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']:continue
    else:print(text[i].upper()[0],end="")