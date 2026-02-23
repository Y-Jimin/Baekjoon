while True:
    edge=list(map(int,input().split()))
    if edge[0]==0 and edge[1]==0 and edge[2]==0:
        break
    c=max(edge)
    edge.pop(edge.index(c))
    if c**2==edge[0]**2+edge[1]**2:
        print("right")
    else:
        print("wrong")