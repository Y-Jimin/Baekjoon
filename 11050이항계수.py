import math
n, k = map(int,input().split())

def combine(n, k):
    ans=1
    for _ in range(k):
        ans*=n
        n-=1
    return int(ans/math.factorial(k))

if k<=n/2:
    print(combine(n,k))
else:
    print(combine(n,n-k))