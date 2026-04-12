import sys
input = sys.stdin.readline
handict = dict()

n=int(input())
hand = list(map(int,input().split()))

for i in hand:
    if i in handict.keys():
        handict[i]+=1
    else:
        handict[i]=1

print(handict)

m=int(input())
find = list(map(int,input().split()))

ans=[]

for i in find:
    if i in handict.keys():
        ans.append(handict[i])
    else:
        ans.append(0)
print(*ans)