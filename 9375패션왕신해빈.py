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


    


#3C1(a+b+c) + 3C2(a+b+c)
#3*(2+2+1) = 15
#4+2+2=8

# 3 -> 3
# 2,1 -> 2+1+(2*1) = 5
# 2,2,1 -> 2+2+1+(2*2 + 2*1 + 2*1)+(2*2*1) = 5+8+4 = 17 = 
# 4,3,2,1 -> 4+3+2+1+(4*3 + 4*2 + 4*1 + 3*2 + 3*1 + 2*1)+(4*3*2 + 4*3*1 + 4*2*1)+(4*3*2*1) = 10+35+44+24 = 
# 4*(3+2+1) + 3*(2+1) + 2*1
# 4*(3*2 + 3*1 + 2*1)