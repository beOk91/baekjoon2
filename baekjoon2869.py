a,b,v=map(int,input().strip().split())
print((v-a)//(a-b)+2 if (v-a)%(a-b)!=0 else (v-a)//(a-b)+1)