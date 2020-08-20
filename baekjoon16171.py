text=input()
keyword=input()
text2=""
for element in text:
    if not(element >='0' and element<='9'):
        text2+=element
print(1 if keyword in text2 else 0)