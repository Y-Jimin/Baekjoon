n=int(input())
grid=[]

for i in range(n):
    grid.append(list(map(int,input().split())))
grid.sort(key=lambda x: (x[1],x[0]))

for i in range(n):
    print(grid[i][0], grid[i][1])
