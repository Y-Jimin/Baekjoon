import sys
from collections import deque

# 1. 빠른 입력을 위해 필수!
input = sys.stdin.readline

n,m = map(int, input().split())
ground=[[] for _ in range(n)]
result=[[-1 for _ in range(m)] for _ in range(n)]
dest=[]

for i in range(n):
    line = list(map(int, input().split()))
    if 2 in line:
        dest = [i, line.index(2)]
    ground[i] = line

queue = deque()

da = [0, 1, 0, -1]
db = [1, 0, -1, 0]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            result[i][j] = 0

def bfs(a,b):
    queue.append((a,b))
    result[a][b] = 0

    while queue:
        (a,b) = queue.popleft()
        for i in range(4):
            next_a = a+da[i]
            next_b = b+db[i]

            if (0<=next_a<n) and (0<=next_b<m) and (result[next_a][next_b] == -1):
                result[next_a][next_b] = result[a][b]+1
                queue.append((next_a, next_b))

bfs(dest[0], dest[1])

for i in range(n):
    print(*result[i])

