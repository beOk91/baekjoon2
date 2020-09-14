text=input()
for element in text:
    print(chr(((ord(element)-65+26-3)%26)+65),end="")
