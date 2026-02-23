n=int(input())
num=list(map(int, input().split()))
num.sort()
num.reverse()

time=0
cnt=1
for i in num:
   time+=i*cnt
   cnt+=1
print(time)