fibo = [[0,0] for _ in range(41)]
# 0인 경우, 1인 경우 미리 저장
fibo[0] = [1, 0]
fibo[1] = [0, 1]

# dynamic programming으로 미리 값 계산
for i in range(2,41):
    fibo[i] = [fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1]]

t = int(input())
for i in range(t):
    n = int(input())
    print(*fibo[n])