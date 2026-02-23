n=int(input())

dp=[-1 for _ in range(n+1)]

dp[0]=0
dp[1]=0

for i in range(2,n+1):
    first = dp[i-1]+1
    if i%2==0:
        second = dp[i//2]+1
    else:
        second=999
    if i%3==0:
        third = dp[i//3]+1
    else:
        third=999
    if min(first, second, third)==first:
        dp[i] = first
    elif min(first, second, third)==second:
        dp[i] = second
    else:
        dp[i] = third

print(dp[n])
