#사이즈 입력
n,m=map(int, input().split())
board=[]

#체스판 모양 입력
for i in range(n):
    line=list(input())
    board.append(line)

cnt=0
min=64
for i in range(n-7):
    for j in range(m-7):
        for newi in range(i, i+8): #시작점이 B인 경우에 대해 계산
            for newj in range(j, j+8):
                if (newi-i)%2 == (newj-j)%2: # B인 경우
                    if board[newi][newj]=='W':
                        cnt+=1
                else:
                    if board[newi][newj]=='B':
                        cnt+=1
        if cnt<min:
            min=cnt
        cnt=0

        for newi in range(i, i+8): #이후 시작점이 W인 경우에 대해 계산
            for newj in range(j, j+8):
                if (newi-i)%2 == (newj-j)%2: # W인 경우
                    if board[newi][newj]=='B':
                        cnt+=1
                else:
                    if board[newi][newj]=='W':
                        cnt+=1
        if cnt<min:
            min=cnt
        cnt=0
        
print(min)