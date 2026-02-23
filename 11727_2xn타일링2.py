n=int(input())

if n==1:
    print(1)
else:
    tile=[0 for _ in range(n+1)]
    tile[0]=1
    tile[1]=1

    for i in range(2, n+1):
        tile[i] = tile[i-1] + 2*tile[i-2]
        tile[i]%=10007

    print(tile[n])


1 - 1
2 - 3
3 - 5
4 - 11
5 - 21