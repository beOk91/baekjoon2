text=input().strip()
arr=[]
first=text[:text.index(min(text))+1]
text=text[text.index(min(text))+1:]
middle=text[:text.index(min(text))+1]
end=text[text.index(min(text))+1:]
arr=sorted([first[::-1],middle[::-1],end[::-1]],key=lambda x:x[0])
print("".join(str(e) for e in arr))