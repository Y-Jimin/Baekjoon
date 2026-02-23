t=int(input())
num=[0 for _ in range(12)]
num[0]=1
num[1]=1
num[2]=2

for i in range(t):
    n=int(input())
    if n<3:
        print(num[n])
    else:
        for j in range(3,n+1):
            num[j] = num[j-1]+num[j-2]+num[j-3]
        print(num[n])

#
#1-1
#2-2
#3-4
#4-7
#5-13