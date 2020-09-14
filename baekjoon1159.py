n=int(input())
player=[0]*26
for _ in range(n):
    player[ ord(input().strip()[0])-97]+=1
print("PREDAJA" if max(player)<5 else "".join(chr(i+97) for i in range(26) if player[i]>=5))