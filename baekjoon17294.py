num=input()
flag=True
if len(num)>=3:
    for i in range(len(num)-2):
        if int(num[i])-int(num[i+1])!=int(num[i+1])-int(num[i+2]):
            flag=False
            break
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if flag else "흥칫뿡!! <(￣ ﹌ ￣)>")
    