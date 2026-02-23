T=int(input())
totalscore=0
score=0
for i in range(T):
    line=input()
    for result in range(len(line)):
        if line[result]=='O':
            for j in range(result,-1,-1):
                if line[j]=='O':
                    score+=1
                else:
                    break
            totalscore+=score
            score=0
        else:
            score=0
    print(totalscore)
    totalscore=0

