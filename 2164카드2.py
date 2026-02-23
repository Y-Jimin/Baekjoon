from collections import deque

n=int(input())
card = deque(range(1,n+1))

while True:
    if len(card)==1:
        break
    card.popleft()
    if len(card)==1:
        break
    card.append(card.popleft())
print(*card)

2468
468
684
84
48
8

123456789
23456789
34567892
4567892
5678924

123
23
32
2

1234
234
342
42
24
