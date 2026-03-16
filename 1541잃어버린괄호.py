hang = input().split('-')
answer = []

for i in hang:
    if i.isdigit():
        answer.append(int(i))
    else:
        a=0
        temp=i.split('+')
        for j in temp:
            a+=int(j)
        answer.append(a)

if len(answer)==1:
    print(answer[0])
else:
    fanswer = answer[0]
    for i in range(1, len(answer)):
        fanswer -= answer[i]
    print(fanswer)