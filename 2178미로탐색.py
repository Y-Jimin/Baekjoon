from collections import deque

n, m = map(int,input().split())
miro = [[] for i in range(n)]
visited = [[False for i in range(m)] for j in range(n)]

for i in range(n):
    miro[i] = list(map(int,input()))

print(miro)
print(visited)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 내에 있고, 처음 방문하는 길(1)이라면?
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))
                
    return miro[n-1][m-1]

print(bfs(0,0))
