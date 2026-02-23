import sys
input=sys.stdin.readline

S=set([])
m=int(input())
for i in range(m):
    act=list(input().split())
    if act[0]=='add' and int(act[1]) not in S:
        S.add(int(act[1]))
    elif act[0]=='remove' and int(act[1]) in S:
        S.remove(int(act[1]))
    elif act[0]=='check':
        if int(act[1]) in S:
            print(1)
        else:
            print(0)
    elif act[0]=='toggle':
        if int(act[1]) in S:
            S.remove(int(act[1]))
        else:
            S.add(int(act[1]))
    elif act[0]=='all':
        S=set([i for i in range(1,21)])
    elif act[0]=='empty':
        S=set([])