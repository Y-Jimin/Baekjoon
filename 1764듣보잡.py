import sys

# 1. 빠른 입력을 위해 sys.stdin.readline 사용 (데이터가 많을 때 필수)
input = sys.stdin.readline

n, m = map(int, input().split())

# 2. 리스트 대신 set(집합)을 사용 (해시 테이블 구조)
never_heard = set()
for _ in range(n):
    never_heard.add(input().strip())

answer = []
for _ in range(m):
    find = input().strip()
    # set에서의 'in' 연산은 평균 O(1)입니다.
    if find in never_heard:
        answer.append(find)

# 3. 사전순 정렬
answer.sort()

# 4. 결과 출력
print(len(answer))
for name in answer:
    print(name)