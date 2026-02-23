from collections import deque

n, m, s = map(int, input().split())
edge = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
for sublist in edge:
    sublist.sort()

def dfs(s):
    visited[s] = True
    print(s, end=" ")
    for i in edge[s]:
        if visited[i]==False:
            dfs(i)

queue = deque()
def bfs(s):
    queue.append(s)
    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in edge[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(s)
print()
visited = [False] * (n+1)
bfs(s)