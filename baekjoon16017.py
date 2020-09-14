num=[]
for _ in range(4):
    num.append(int(input()))
print("ignore" if num[0] in [8,9] and num[-1] in [8,9] and num[1]==num[2] else "answer")