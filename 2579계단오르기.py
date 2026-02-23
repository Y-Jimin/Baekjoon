n=int(input())
step=[]
dp=[0 for _ in range(n+1)]
for i in range(n):
    step.append(int(input()))

if n==1:
    dp[1]=step[0]
    print(dp[1])
elif n==2:
    dp[2]=step[0]+step[1]
    print(dp[2])
else:
    dp[1]=step[0]
    dp[2]=step[0]+step[1]
    for i in range(3, n+1):
        dp[i] = max(step[i-1]+dp[i-2], step[i-1]+step[i-2]+dp[i-3])
    print(dp[n])