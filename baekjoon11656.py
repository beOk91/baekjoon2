s=input().strip()
print("\n".join(sorted(s[i:len(s)] for i in range(len(s)))))