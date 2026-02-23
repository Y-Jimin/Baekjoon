count = 0

def countIsland(x,y,land):
    global count
    if x<0 or x>len(land[0]) or y<0 or y>len(land):
        return 0
    rows=len(land)
    cols=len(land[0])
    for r in range(rows):
        for c in range(cols):
            if land[r][c] == 1:
                count+=1
                floodFill(r,c,land)
    return

def floodFill(x,y,land):
    if x<0 or x>len(land[0]) or y<0 or y>len(land):
        return
    
    land[x][y] = 0
    
    if land[x][y]==1:
        floodFill(x+1, y, land) #상
        floodFill(x-1, y, land) #우
        floodFill(x, y+1, land) #하
        floodFill(x, y-1, land) #좌
    else:
        return

t=int(input())

for i in range(t): # 전체 시행 횟수
    count=0
    m,n,k=map(int, input().split())
    land = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(k): # 배추 위치 입력받기
        a,b=map(int, input().split())
        land[b][a] = 1
    countIsland(b,a,land)
    print(count)