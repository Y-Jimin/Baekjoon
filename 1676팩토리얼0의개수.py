def factorial(n):
    if n==0:
        return 1
    return factorial(n-1)*n

n=int(input())
line=str(factorial(n))
cnt=0

for i in range(len(line)-1,-1,-1):
    if line[i]=='0':
        cnt+=1
    else:
        break
print(cnt)