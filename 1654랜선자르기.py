k, n = map(int, input().split())
lan=[]
flag=0

for i in range(k):
    lan.append(int(input()))

low = 1
high = max(lan)
result=0

while low <= high:
    cnt = 0
    mid = (low+high)//2

    for i in lan:
        cnt+=i//mid
    
    if cnt<n:
        high=mid-1
    elif cnt>=n:
        result=mid
        low=mid+1

print(result)