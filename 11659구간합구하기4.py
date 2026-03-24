n,m = map(int, input().split())
num = list(map(int, input().split()))

sumfix = [0 for _ in range(n)]
sumfix[0]=num[0]

for i in range(1,n):
    sumfix[i] = sumfix[i-1]+num[i]

for i in range(m):
    i,j = map(int,input().split())
    if i <= 1:
        print(sumfix[j-1])
    else:
        print(sumfix[j-1] - sumfix[i-2])