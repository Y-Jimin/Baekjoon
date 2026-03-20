from collections import deque

n,k = map(int,input().split())
visited=[0 for i in range(100001)]
queue = deque()

def bfs(n):
    visited[n]+=1
    queue.append(n)

    while queue:
        current = queue.popleft()
        sick = [current+1, current-1, 2*current]
        
        for i in sick:
            next_pos = i
            if (0<=next_pos<=100000) and (visited[next_pos] == 0):
                queue.append(next_pos)
                visited[next_pos] = visited[current]+1
            if next_pos == k:
                break
    return visited[k]-1

print(bfs(n))