n=int(input())
cnt=0
com = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

m=int(input())
for i in range(m):
    a,b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)

def dfs(n):
    global cnt
    visited[n] = True
    
    for i in com[n]:
        if visited[i] == False:
            cnt+=1
            dfs(i)

dfs(1)
print(cnt)