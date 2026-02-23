n,m=map(int,input().split())
line=list(map(int,input().split()))

max=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if line[i]+line[j]+line[k]<=m and max<line[i]+line[j]+line[k]:
                max=line[i]+line[j]+line[k]
print(max)