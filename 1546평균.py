T=int(input())
newScore=0
score=list(map(int,input().split()))
for i in range(T):
    newScore+=score[i]/max(score)*100
print(newScore/T)