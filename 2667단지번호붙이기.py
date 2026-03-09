import sys
# 재귀 깊이 제한 해제 (DFS 필수)
sys.setrecursionlimit(2000)

n=int(input())
ground=[[] for i in range(n)]
visited=[[False for i in range(n)] for i in range(n)]
allcnt = 0
cntls = []

for i in range(n):
    ground[i]=(list(map(int, input())))

def dfs(x,y):
    global cnt
    cnt+=1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y]=True

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (n>nx>=0)and(n>ny>=0):
            if visited[nx][ny]==False:
                if ground[nx][ny]==1:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if ground[i][j]==1 and visited[i][j]==False:
            allcnt += 1
            cnt = 0
            dfs(i,j)
            cntls.append(cnt)
print(allcnt)
cntls.sort()
for i in range(len(cntls)):
    print(cntls[i])