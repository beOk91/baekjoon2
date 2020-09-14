n=int(input())
for i in range(1,n+1):
    text=input()
    print("String #{}".format(i))
    print("".join(chr((ord(element)-65+1+26)%26+65) for element in text))
    if i!=n:print()