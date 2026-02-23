n=int(input())
for i in range(n):
    address=list(map(int,input().split()))
    if address[2]%address[0]!=0:
        b=address[2]//address[0]+1
        a=(address[2]%address[0])*100
    else:
        b=address[2]//address[0]
        a=address[0]*100
    print(a+b)