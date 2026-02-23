n=int(input())

start=1
finish=1
tum=6
cnt=1

while True:
    if start<=n<=finish:
        print(cnt)
        break
    finish+=tum
    start=finish-tum+1
    tum+=6
    cnt+=1
