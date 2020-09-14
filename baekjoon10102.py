v=int(input())
text=input()
a=sum(1 if element=="A" else 0 for element in text)
print("Tie" if v-a==a else "A" if v-a<a else "B")