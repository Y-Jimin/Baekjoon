import sys # 시간 초과 뜰 때, 이거 먼저 고려하기
input=sys.stdin.readline # 시간 초과 뜰 때, 이거 먼저 고려하기
n=int(input())
stack=[]

for i in range(n):
    act=list(input().split())
    if act[0]=='push':
        stack.append(int(act[1]))
    elif act[0]=='pop':
        if stack==[]:
            print(-1)
        else:
            print(stack.pop())
    elif act[0]=='size':
        print(len(stack))
    elif act[0]=='empty':
        if stack==[]:
            print(1)
        else:
            print(0)
    else:
        if stack==[]:
            print(-1)
        else:
            print(stack[-1])