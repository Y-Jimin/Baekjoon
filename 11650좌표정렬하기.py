n=int(input())
grid=[[0,0] for i in range(n)]
for i in range(n):
    grid[i][0],grid[i][1]=map(int,input().split())

grid.sort(key=lambda x: (x[0],x[1]))
for i in range(n):
    print(grid[i][0], grid[i][1])