import sys
input=sys.stdin.readline

n,k = map(int, input().split())
coin=[]

for i in range(n):
    coin.append(int(input()))
coin.reverse()

cnt=0

while k!=0:
    for i in coin:
        if k>=i:
            cnt+=k//i
            k=k%i
            break
print(cnt)