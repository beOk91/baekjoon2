text=input().strip().split()
a=("".join(i[0].upper() for i in text))
print(a)
print("U-C-P-C" in a)
result=""
for i in range(len(a)):
    if a[i] not in ["U","C","P","C"]:
        continue
    else:
        result+=a[i]
print(result)