text=input()
len(text)//2
print(1 if text[0:len(text)//2]==text[::-1][0:len(text)//2] else 0)
