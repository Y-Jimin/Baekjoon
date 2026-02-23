def howlong(num):
    cnt=0
    while num!=0:
        num=num//10
        cnt+=1
    return cnt

def devideSum(ni):
    namuji=10
    mok=1
    temp=ni
    tempAns=ni
    for i in range(howlong(ni)):
        tempAns+=temp%namuji//mok
        namuji*=10
        mok*=10
    return tempAns

n=int(input())
checker=0

for i in range(1,n):
    answer=devideSum(i)
    if answer==n:
        checker=1
        print(i)
        break
if checker==0:
    print(0)