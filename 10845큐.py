#import sys # 시간 초과 뜰 때, 이거 먼저 고려하기
#input=sys.stdin.readline # 시간 초과 뜰 때, 이거 먼저 고려하기
T=int(input())

def pushQ(n):
    global rear
    global queue
    queue.append(n)
    rear+=1

def popQ():
    global front
    global queue
    front+=1
    return queue[front-1]

queue=[]
front=0
rear=0

for i in range(T):
    act=list(input().split())
    if act[0]=='push':
        pushQ(int(act[1]))
    elif act[0]=='pop':
        if front==rear:
            print(-1)
        else:
            print(popQ())
    elif act[0]=='size':
        print(rear-front)
    elif act[0]=='empty':
        if front==rear:
            print(1)
        else:
            print(0)
    elif act[0]=='front':
        if front==rear:
            print(-1)
        else:
            print(queue[front])
    elif act[0]=='back':
        if front==rear:
            print(-1)
        else:
            print(queue[rear-1])