import decimal
n=int(input().strip())
score_sum=0
for _ in range(n):
    score=input()
    if len(score)!=3:score=score.replace("0","9");score=score.replace("6","9")
    score_sum+=int(score)
print(round(decimal.Decimal(score_sum)/decimal.Decimal(n)+decimal.Decimal(0.01),0))