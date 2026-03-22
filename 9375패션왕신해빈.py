t=int(input())
closet = dict()

def count(ls):
    answer=1
    for i in ls:
        answer*=(i+1)
    return answer-1

for i in range(t):
    closet = {}
    cnt = []
    n=int(input())
    for j in range(n):
        name, key = input().split()
        if key not in closet:
            closet[key] = []
        closet[key].append(name)
    for j in closet.keys():
        cnt.append(len(closet[j]))
    print(count(cnt))