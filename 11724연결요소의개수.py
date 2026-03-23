import sys
sys.setrecursionlimit(10**6)
# 1. 빠른 입력을 위해 필수!
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = set()

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(a):
    visited[a] = True
    result.add(a)
    for i in graph[a]:
        if visited[i] == False:
            dfs(i)
cnt=0
while True:
    if result == set(range(1,n+1)):
        break
    for i in range(1,n+1):
        if i not in result:
            cnt+=1
            dfs(i)
print(cnt) 